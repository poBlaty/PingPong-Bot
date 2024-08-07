import enum
import pprint

from typing import NamedTuple

import excel_part.xmain as xl
import excel_part.xfunctoconcl as cl

# from main import applicationMessageToAdmin, sendToUser

import redis


class PlaceInRating(NamedTuple):
    raiting: int
    place: int


class UserRating(NamedTuple):
    mouth_year: str
    listRaiting: PlaceInRating


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
    in_process: int = 2
    not_registered: int = 3


db = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)


class User:
    id: str
    name: str = None
    surname: str = None

    def __init__(self, tid: str):
        self.id = tid

    def isUserSignIn(self) -> int:
        if self.__class__ is not User:
            return StatusRegistration.registered.value

        if len(db.hgetall(self.id)) != 0:
            return StatusRegistration.in_process.value  # in process

        return StatusRegistration.not_registered.value

    def signIn(self, surname: str, name: str, phone_number: str):

        if self.isUserSignIn() == StatusRegistration.registered.value:
            return True  # application is already created

        user_data = {'name': name,
                     'surname': surname,
                     'phone_number': phone_number
                     }

        db.hset(self.id, mapping=user_data)
        return True

    def checkFullName(self):
        pass

    def checkPhoneNumber(self):
        pass

    def getId(self):
        return self.id

    def choosePlayer(self, name: str, surname: str) -> int:
        if xl.GetIdByName(name=name, surename=surname) is None:
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
        age = xl.BirthdayBase(self.id).split('-')
        bage = f'{age[2]}.{age[1]}.{age[0]}'
        gender = xl.GenderBase(self.id)
        raiting_FNTR = int(xl.RaitingFNTRBase(self.id))
        category = xl.СategoryBase(self.id)
        rating, place = cl.PlaceInRaitingKOFNT(self.surname + " " + self.name)
        return Procfile(year=bage, gender=gender, rateKOFNT=rating, rateFNTR=raiting_FNTR, category=category,
                        place=place)

    def getStatistics(self):
        pass

    def __getGraphic(self):
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
        self.surname = xl.SurenameBase(tid)

    def getRating(self):
        result = []
        l = cl.YearPlaceInRaitingKOFNT(self.surname + " " + self.name)
        for mouth_year, rating_list in l:
            place = PlaceInRating(raiting=rating_list[0], place=rating_list[1])
            result.append(UserRating(mouth_year, place))
        return result


class Referee(Player):
    pass


class Trainer(Player):

    def playersStatistics(self):
        pass


class Admin(Trainer, Referee):

    @classmethod
    def getApplicationToReg(cls, tid):
        data = db.hgetall(tid)
        print(data)
        text = (f"пользователь подал заявку на регистрацию\n"
                f"Имя: {data['name']}, Фамилия: {data['surname']}, Номер: {data['phone_number']}, ID: {tid}\n"
                f"нажмите кнопку для подтверждения")
        return xl.FindByRole('Админ'), text
        # applicationMessageToAdmin(adminID, text)

    def getListOfRedUsers(self):  # in the next update
        pass

    def authterizeUser(cls, tid):  # in the next update
        pass

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
        year = 2024
        comps = cl.CompsValueYear(year=year, name='')
        matches = cl.MatchValueYear(year=year, name='')
        sets = cl.SetsValueYear(year=year, name='')
        points = cl.PointsValueYear(year=year, name='')
        return CommonData(comps=comps, matches=matches, sets=sets, points=points)

    # @classmethod
    # def getAllAdmins(cls):
    #


def auntendefication(tid: str) -> (User, Player, Trainer, Admin):
    cash_time = 600  # 10 minutes
    try:
        cash = db.get(tid)
    except redis.exceptions.ResponseError:
        return User(tid)

    if cash is not None:
        if cash == 'Админ':  # '6126011940'
            return Admin(tid)
        if cash == 'Тренер':
            return Trainer(tid)
        if cash == 'Судья':
            return Referee(tid)
        if cash == 'Игрок':
            return Player(tid)

    if xl.IsIdInBase(tid):
        role = xl.GetRoles(tid)
        if 'Админ' in role:
            db.setex(tid, cash_time, 'Админ')  # add to cash
            return Admin(tid)
        if 'Тренер' in role:
            db.setex(tid, cash_time, 'Тренер')
            return Trainer(tid)
        if 'Судья' in role:
            db.setex(tid, cash_time, 'Судья')
            return Referee(tid)
        if 'Игрок' in role:
            db.setex(tid, cash_time, 'Игрок')
            return Player(tid)

    # db.setex(tid, cash_time, 'Пользователь')
    return User(tid)


def auth(func):
    async def inner(*args):
        user = auntendefication(657253131)  # message.from_user.id 657253131 kate
        return await func(*args, user) # kwargs['state']

    return inner


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
