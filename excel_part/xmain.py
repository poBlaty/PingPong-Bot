import pandas as pd

def IDBase(num:int) -> str:                          #ID из "База"
    return df_base['ID'].values[num]

def SurenameBase(num:int) -> str:                    #Фамилия из "База"
    return df_base['Имя'].values[num]

def NameBase(num:int) -> str:                        #Имя из "База"
    return df_base['Фамилия'].values[num]

def GenderBase(num:int) -> str:                      #Пол из "База"
    return df_base['Пол'].values[num]

def RaitingKOFNTBase(num:int) -> int:                #Рейтинг КОФНТ из "База"
    return df_base['Рейтинг КОФНТ'].values[num]

def RaitingFNTRBase(num:int) -> int:                 #Рейтинг ФНТР из "База"
    return df_base['Рейтинг ФНТР'].values[num]

def RaitingRTTFBase(num:int) -> int:                 #Рейтинг РТТФ из "База"
    return df_base['Рейтинг РТТФ'].values[num]

def BirthdayBase(num:int) -> str:                    #Дата рождения из "База"
    return df_base['Дата рождения'].values[num]

def СategoryBase(num:int) -> str:                    #Разряд из "База"
    return df_base['Спортивный разряд'].values[num]

def CityBase(num:int) -> str:                        #Город из "База"
    return df_base['Город'].values[num]

def Name1List(num:int) -> str:                       #Имя 1 из "Список матчей"
    return df_match['Имя 1'].values[num]

def Name2List(num:int) -> str:                       #Имя 2 из "Список матчей"
    return df_match['Имя 2'].values[num]

def Set1List(num:int) -> str:                                                                      #Партия 1 из "Список матчей"
    return (f'{int(df_match["Партия 1 1"].values[num])}:{int(df_match["Партия 1 2"].values[num])}')
def Set2List(num:int) -> str:                                                                      #Партия 2 из "Список матчей"
    return (f'{int(df_match["Партия 2 1"].values[num])}:{int(df_match["Партия 2 2"].values[num])}')
def Set3List(num:int) -> str:                                                                      #Партия 3 из "Список матчей"
    return (f'{int(df_match["Партия 3 1"].values[num])}:{int(df_match["Партия 3 2"].values[num])}')
def Set4List(num:int) -> str:                                                                      #Партия 4 из "Список матчей"
    return (f'{int(df_match["Партия 4 1"].values[num])}:{int(df_match["Партия 4 2"].values[num])}')
def Set5List(num:int) -> str:                                                                      #Партия 5 из "Список матчей"
    return (f'{int(df_match["Партия 5 1"].values[num])}:{int(df_match["Партия 5 2"].values[num])}')
def Set6List(num:int) -> str:                                                                      #Партия 6 из "Список матчей"
    return (f'{int(df_match["Партия 6 1"].values[num])}:{int(df_match["Партия 6 2"].values[num])}')
def Set7List(num:int) -> str:                                                                      #Партия 7 из "Список матчей"
    return (f'{int(df_match["Партия 7 1"].values[num])}:{int(df_match["Партия 7 2"].values[num])}')

def GlobalScoreList(num:int) -> str:                #Общий счет из "Список матчей"
    return df_match['Общий счет'].values[num]

def CompNameList(num:int) -> str:
    return df_match['Название соревнований'].values[num]


df_base = pd.read_excel("D:\Git\TT\PingPong-Bot\data\База.xlsx")
df_match = pd.read_excel("D:\Git\TT\PingPong-Bot\data\Список матчей.xlsx")

print(GlobalScoreList(0))
