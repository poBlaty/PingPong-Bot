import datetime
import enum
import logging

from typing import NamedTuple

import aiofiles

import core.excel_part.xmain as xl
import core.excel_part.xfunctoconcl as cl

from redis import Redis


class PlaceInRating(NamedTuple):
    rating: int
    place: int


class UserRating(NamedTuple):
    mouth_year: str
    listRating: PlaceInRating


class Procfile(NamedTuple):
    year: str
    gender: str
    rateKOFNT: int
    rateFNTR: int
    category: str
    place: int


class CommonData(NamedTuple):
    comps: int
    matches: int
    sets: int
    points: int


class BestWins(NamedTuple):
    tourName: str
    player_1: str
    ranking_1: int
    total_count: str
    player_2: str
    ranking_2: str
    count: str


class Match(NamedTuple):
    player_1: str
    player_2: str
    score: str
    result_parties: str


class Competition(NamedTuple):
    name: str
    plays: list


class BestMatches(NamedTuple):
    name: str
    rating_1: int
    rating_2: int
    player_1: str
    player_2: str
    score: str
    result_parties: str


class StatusRegistration(enum.Enum):
    registered: int = 1
    access_denied: int = 2
    in_process: int = 3
    not_registered: int = 4
    banned: int = 0


class ErrorCodes(enum.Enum):
    no_error: int = 1
    error_len: int = 0
    error_symbol: int = 0


class User:
    # id: str
    # name: str = None
    # surname: str = None

    def __init__(self, tid: str | int):
        self.id = tid
        self.name = 'Егор'
        self.surname = 'Зинчук'
        if xl.IsIdInBase(tid):
            self.name = xl.NameBase(tid)
            self.surname = xl.SurnameBase(tid)

    async def _open_banned_file(self) -> bool:
        async with aiofiles.open("data/bannedUsers.txt", 'r') as f:
            _tid = (await f.readline())[:-1]
            while len(_tid) != 0:
                if _tid == str(self.id):
                    return True
                _tid = (await f.readline()).replace('\n', '')
            return False

    async def isUserSignIn(self, db: Redis) -> int:

        if await self._open_banned_file():
            return StatusRegistration.banned.value

        return int((await db.hget(str(self.id), 'reg')))

    async def signIn(self, tid: int|str, name: str, phone_number: str, db: Redis):
        role = 'User'
        try:
            role = xl.GetRoles(tid)
        except:
            logging.critical("excel doesn't work")

        user_data = {
            'status': role,
            'name': name,
            'phone_number': str(phone_number),
            'reg': StatusRegistration.in_process.value
        }

        await db.hset(str(tid), mapping=user_data)

    @staticmethod
    def checkFullName(name: str):
        for i in range(len(name)):
            if name[i].lower() in '1234567890<>_+=№;:{?.,}~!@#$%^&*()|/\\\'\"':
                return ErrorCodes.error_symbol.value
        return ErrorCodes.no_error.value

    @staticmethod
    def checkPhoneNumber(num: str):
        if num[0] == '+':
            num = num[1:]

        if len(num) == 11 and (num[0] == '7' or num[0] == '8'):
            try:
                int(num)
                return ErrorCodes.no_error.value
            except:
                return ErrorCodes.error_symbol.value
        else:
            return ErrorCodes.error_len.value

    def getId(self):
        return self.id

    def choosePlayer(self, name: str, surname: str) -> int:
        if xl.GetIdByName(surname=surname, name=name) is None:
            return -1  # not in excel or name or surname are wrong
        self.name = name
        self.surname = surname
        return 1

    def getbestWins(self):
        data = cl.BestWins(self.surname + " " + self.name, 5)
        l = []
        for i in data:
            if data[0] != i:
                l.append(BestMatches(name=i[0], player_1=i[1], rating_1=i[2], score=i[3], player_2=i[4], rating_2=i[5],
                                     result_parties=i[6]))
        return l

    def getLastMatches(self):
        data = cl.LastComp(self.surname + " " + self.name)
        l = []
        for i in data:
            if data[0] != i:
                l.append(Match(player_1=i[0], player_2=i[2], score=i[1],
                               result_parties=i[3]))
        return Competition(data[0], l)

    def getProcfile(self):
        age = str(xl.BirthdayBase(self.id)).split('-')  # could get a nan Egor fix this
        bage = f'{age[2]}.{age[1]}.{age[0]}' if len(age) > 1 else age[0]
        gender = xl.GenderBase(self.id)
        raiting_FNTR = xl.RaitingFNTRBase(self.id)
        category = xl.СategoryBase(self.id)
        rating, place = None, None
        if cl.PlaceInRaitingKOFNT(str(self.surname) + " " + str(self.name)) is not None:
            rating, place = cl.PlaceInRaitingKOFNT(self.surname + " " + self.name)  # rating, place
        return Procfile(year=bage, gender=gender, rateKOFNT=rating, rateFNTR=raiting_FNTR, category=category,
                        place=place)

    def getRating(self):
        result = []
        l = cl.YearPlaceInRaitingKOFNT(str(self.surname) + " " + str(self.name))
        for mouth_year, rating_list in l:
            place = PlaceInRating(rating=rating_list[0], place=rating_list[1])
            result.append(UserRating(mouth_year, place))
        return result

    def getStatistics(self):
        pass


    def registrationOnTour(self):
        pass

    def __getFileToTour(self):
        pass

    def matchStatistics(self):
        pass


class Player(User):
    def __init__(self, tid: str):
        super().__init__(tid)
        self.name = xl.NameBase(tid)
        self.surname = xl.SurnameBase(tid)


class Referee(Player):
    pass


class Trainer(Player):

    def playersStatistics(self):
        pass


class Admin(Trainer, Referee, User):

    @classmethod
    async def getApplicationToReg(cls, tid, db: Redis):
        name = await db.hget(str(tid), 'name')
        phone = await db.hget(str(tid), 'phone_number')
        text = (f"пользователь подал заявку на регистрацию\n"
                f"ФИО: {name}, Номер: {phone}, ID: {tid}\n"
                f"нажмите кнопку для подтверждения")
        return text
        # applicationMessageToAdmin(adminID, text)
        #xl.FindByRole('Админ'),

    def getListOfRedUsers(self):  # in the next update
        pass

    def authterizeUser(cls, tid):  # in the next update
        pass

    @classmethod
    def acceptUser(cls, tid):
        pass

    @classmethod
    def cancelUser(cls, tid, db: Redis):
        db.hdel(tid)

    @classmethod
    def changeUserName(cls, tid, name, surname, db: Redis):
        db.hset(tid, "name", name)
        db.hset(tid, "surname", surname)

    @classmethod
    def changeUserPhone(cls, tid, phone, db: Redis):
        db.hset(tid, "phone_number", phone)

    # async def toWriteUser(self, name: str, surname: str):
    #     if xl.IsIdInBase(xl.GetIdByName(name=name, surename=surname)) is True:
    #         await sendToUser(xl.GetIdByName(name=name, surename=surname))
    #         return True
    #     return False

    def notification(self):
        pass

    def handleFiles(self):
        pass

    @classmethod
    def getCommonData(cls):
        year = datetime.date.today().strftime("%Y") #2024
        comps = cl.CompsValueYear(year=year, name='')
        matches = cl.MatchValueYear(year=year, name='')
        sets = cl.SetsValueYear(year=year, name='')
        points = cl.PointsValueYear(year=year, name='')
        return CommonData(comps=comps, matches=matches, sets=sets, points=points)

    # @classmethod
    # def getAllAdmins(cls):
    #


if __name__ == '__main__':  # 1134175573 '6126011940' 858380684
    # user = signIn(8583806846,'qwer','rdtu','23453476')
    # event = {
    #     'qwer':345,
    #     'asdf':6789
    # }
    # db.hset('sensor:sensor1', mapping=event)
    # db.setex(123, 100, 'Тренер')
    # print(db.hget('sensor:sensor1', 'asdf'))
    # db.hdel('sensor:sensor1', 'asdf')
    # print(db.keys())
    # print(xl.FindByRole('Админ'))
    # print(db.get(6126011940))
    print(Admin(1134175573).getbestWins())
    # pass
