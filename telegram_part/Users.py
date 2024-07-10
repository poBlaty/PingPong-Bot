import pprint

from typing import NamedTuple

import excel_part.xmain as xl
import excel_part.xfunctoconcl as cl

# from main import applicationMessageToAdmin, sendToUser

import redis


class Procfile(NamedTuple):
    year: str
    gender: str
    rateKOFNT: int
    rateFNTR: int
    category: str


class BestWins(NamedTuple):
    tourName: str
    player_1: str
    ranking_1: int
    total_count: str
    player_2: str
    ranking_2: str
    count: str


db = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)


class User:
    id: str
    name: str
    surname: str

    def __init__(self, tid: str):
        self.id = tid

    def isUserSignIn(self) -> bool:
        user = auntendefication(self.id)
        if user is not User:
            return True  # already reg

        if db.hgetall(self.id) is not None:
            return True  # in process
        return False

    def signIn(self, surname: str, name: str, phone_number: str):

        if self.isUserSignIn():
            return True  # application is already created

        user_data = {'name': name,
                     'surname': surname,
                     'phone_number': phone_number,
                     'status': False
                     }

        db.hset(self.id, mapping=user_data)
        Admin.getApplicationToReg(tid=self.id)  ## send to all Admins
        return True

    def getId(self):
        return self.id

    def choosePlayer(self, name: str, surname: str) -> int:
        if xl.GetIdByName(name=name, surename=surname) is None:
            return -1  # not in excel or name or surname are wrong
        self.name = name
        self.surname = surname
        return 1

    def bestWins(self):
        cl.BestWins(self.surname + " " + self.name)

        return cl.BestWins(self.surname + " " + self.name)

    def getLastMatches(self):
        return cl.LastComp(self.surname + " " + self.name)

    def getProcfile(self):
        bage = xl.BirthdayBase(self.id)
        gender = xl.GenderBase(self.id)
        raiting_1 = xl.RaitingKOFNTBase(self.id)
        raiting_2 = xl.RaitingFNTRBase(self.id)
        category = xl.СategoryBase(self.id)
        return Procfile(year=bage, gender=gender, rateKOFNT=raiting_1, rateFNTR=raiting_2, category=category)

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

    def commonInfo(self):
        pass

    def employees(self):
        pass

    def commonStatistics(self):
        pass

    def archivePDF(self):
        pass

    def matchResultsPDF(self):
        pass

    def documentsPDF(self):
        pass

    def rating(self, range: int = 10):
        pass


class Player(User):
    def __init__(self, tid: str):
        super().__init__(tid)
        self.name = xl.NameBase(tid)
        self.surname = xl.SurenameBase(tid)


class Referee(Player):
    pass


class Trainer(Player):

    def playersStatistics(self):
        pass


class Admin(Trainer, Referee):

    @classmethod
    def getApplicationToReg(cls, tid):
        data = db.hgetall(tid)

        text = (f"пользователь подал заявку на регистрацию "
                f"{data['name']}, {data['surname']}, {data['phone_number']}, ID:{tid}"
                f"нажмите кнопку для подтвержения")
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


def auntendefication(tid: str) -> (User, Player, Trainer, Admin, User):
    cash_time = 600  # 10 minutes
    cash = db.get(tid)

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


# def auth(func):
#     def inner(*args, **kwargs):
#         # user = auntendefication(message.from_user.id)
#         # print(user)
#         return func(*args, **kwargs)
#
#     return inner


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
    pass
