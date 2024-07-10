import pandas as pd


def IsIdInBase(ID: str) -> bool:                #Есть ли в базе такой id
    for i in range(len(df_base)):
        if ID == df_base["ID"].values[i]:
            return True
    return False


def GetRoles(ID: str) -> list:                  #Роли человека по id
    roles = []
    rolesBase = ["Игрок", "Тренер", "Судья", "Админ"]
    for i in range(len(df_base)):
        if ID == df_base["ID"].values[i]:
            for j in rolesBase:
                if df_base[j].values[i] == 1:
                    roles.append(j)
            break
    return roles


def FindByRole(role: str) -> list:
    id = []
    for i in range(len(df_base)):
        if df_base[role].values[i] == 1:
            id.append(df_base["ID"].values[i])
    return id


def SurenameBase(ID: str) -> str:  # Фамилия из "База"
    for i in range(len(df_base)):
        if ID == df_base["ID"].values[i]:
            return df_base['Фамилия'].values[i]


def NameBase(ID: str) -> str:  # Имя из "База"
    for i in range(len(df_base)):
        if ID == df_base["ID"].values[i]:
            return df_base['Имя'].values[i]


def GetIdByName(surename: str, name: str) -> str:                # ID по имени
    fullname = surename + name
    for i in range(len(df_base)): 
        if str(fullname).replace(' ', '').lower() == str(df_base["Фамилия"].values[i]).lower() + str(df_base["Имя"].values[i]).lower():
            return str(int(df_base["ID"].values[i]))
    return 0


def GenderBase(ID: str) -> str:  # Пол из "База"
    for i in range(len(df_base)):
        if ID == df_base["ID"].values[i]:
            return df_base['Пол'].values[i]


def RaitingKOFNTBase(ID: str) -> int:  # Рейтинг КОФНТ из "База"
    for i in range(len(df_base)):
        if ID == df_base["ID"].values[i]:
            return df_base['Рейтинг КОФНТ'].values[i]


def RaitingFNTRBase(ID: str) -> int:  # Рейтинг ФНТР из "База"
    for i in range(len(df_base)):
        if ID == df_base["ID"].values[i]:
            return df_base['Рейтинг ФНТР'].values[i]


def BirthdayBase(ID: str) -> str:  # Дата рождения из "База"
    for i in range(len(df_base)):
        if ID == df_base["ID"].values[i]:
            return df_base['Дата рождения'].values[i]


def СategoryBase(ID: str) -> str:  # Разряд из "База"
    for i in range(len(df_base)):
        if ID == df_base["ID"].values[i]:
            return df_base['Дата рождения'].values[i]


def CityBase(ID: str) -> str:  # Город из "База"
    for i in range(len(df_base)):
        if ID == df_base["ID"].values[i]:
            return df_base['Город'].values[i]


def Name1List(num: int) -> str:  # Имя 1 из "Список матчей"
    return df_match['Имя 1'].values[num]


def Name2List(num: int) -> str:  # Имя 2 из "Список матчей"
    return df_match['Имя 2'].values[num]


def Set1List(num: int) -> str:  # Партия 1 из "Список матчей"
    return (f'{int(df_match["Партия 1 1"].values[num])}:{int(df_match["Партия 1 2"].values[num])}')


def Set2List(num: int) -> str:  # Партия 2 из "Список матчей"
    return (f'{int(df_match["Партия 2 1"].values[num])}:{int(df_match["Партия 2 2"].values[num])}')


def Set3List(num: int) -> str:  # Партия 3 из "Список матчей"
    return (f'{int(df_match["Партия 3 1"].values[num])}:{int(df_match["Партия 3 2"].values[num])}')


def Set4List(num: int) -> str:  # Партия 4 из "Список матчей"
    return (f'{int(df_match["Партия 4 1"].values[num])}:{int(df_match["Партия 4 2"].values[num])}')


def Set5List(num: int) -> str:  # Партия 5 из "Список матчей"
    return (f'{int(df_match["Партия 5 1"].values[num])}:{int(df_match["Партия 5 2"].values[num])}')


def Set6List(num: int) -> str:  # Партия 6 из "Список матчей"
    return (f'{int(df_match["Партия 6 1"].values[num])}:{int(df_match["Партия 6 2"].values[num])}')


def Set7List(num: int) -> str:  # Партия 7 из "Список матчей"
    return (f'{int(df_match["Партия 7 1"].values[num])}:{int(df_match["Партия 7 2"].values[num])}')


def GlobalScoreList(num: int) -> str:  # Общий счет из "Список матчей"
    return df_match['Общий счет'].values[num]


def CompNameList(num: int) -> str:              # Название соревнований
    return df_match['Название соревнований'].values[num]


df_base = pd.read_excel("data/База.xlsx")
df_match = pd.read_excel("data/Список матчей.xlsx")
