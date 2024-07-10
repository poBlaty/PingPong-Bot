import pprint

from typing import NamedTuple

import excel_part.xmain as xl
import excel_part.xfunctoconcl as cl

import redis


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
        pass

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

    def authterizeUser(self):
        pass

    def writeUser(self):
        pass

    def notification(self):
        pass

    def handleFiles(self):
        pass


def auntendefication(tid: str) -> (User, Player, Trainer, Admin, User):
    cash_time = 600  # 10 minutes
    cash = db.get(tid)

    if cash is not None:
        if cash == 'Тренер':
            return Trainer(tid)
        if cash == 'Админ':  # '6126011940'
            return Admin(tid)
        if cash == 'Судья':
            return Referee(tid)
        if cash == 'Игрок':
            return Player(tid)

    # if xl.IsIdInBase(tid):
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

    return User(tid)


def signIn(tid: str, username: str = None, name: str = None, phone_number: str = None) -> User:
    user = auntendefication(tid)
    if user is not User:
        return user

    db.hset(tid, name, username, phone_number)
    for AdminId in xl.FindByRole('Admin'):  ## send to all Admins
        Admin.authterizeUser(AdminId)

    return User(tid)


def auth(func):
    def inner(message, _):
        user = auntendefication(str(message.from_user.id))
        # print(user)
        return func(tid=message, user=user)

    return inner


if __name__ == '__main__':
    # r.set('foo', 'baar')
    print(db.get('1134175573'))
    # user = User('1134175573')
    user = auntendefication('1134175573') # '6126011940'
    print(user)
    # user.choosePlayer('Егор', 'Зинчук')
    # pprint.pprint(user.bestWins())
