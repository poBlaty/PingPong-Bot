import pandas as pd

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

def Name2List(num:int) -> str:                       #Имя 1 из "Список матчей"
    return df_match['Имя 2'].values[num]

def Set1() -> str:                                   #Партия 1 из "Список матчей"
    pass
def Set2() -> str:                                   #Партия 2 из "Список матчей"
    pass
def Set3() -> str:                                   #Партия 3 из "Список матчей"
    pass
def Set4() -> str:                                   #Партия 4 из "Список матчей"
    pass
def Set5() -> str:                                   #Партия 5 из "Список матчей"
    pass
def Set6() -> str:                                   #Партия 6 из "Список матчей"
    pass
def Set7() -> str:                                   #Партия 7 из "Список матчей"
    pass

def GlobalScore(num:int) -> str:                     #Общий счет из "Список матчей"
    return df_match['Общий счет'].values[num]

def BetsWinsList() -> str:                           #Лучшие победы игрока из "Список матчей"
    pass

def LastMathchesList() -> str:                       #Список последних матчей из "Список матчей"
    pass 

def CounterMatchesList() -> int:                     #Кол-во матчей из "Список матчей"
    pass

def CounterSetsList() -> int:                        #Кол-во партий из "Список матчей"
    pass

def CounterPointsList() -> int:                      #Кол-во очков из "Список матчей"
    pass

def GovermentKOFNT() -> str:                         #Список важных шишек федерации
    pass

def CompsToRegistr() -> str:                         #Список труниров для регистрации
    pass

def KOFNTDocumentsOutput() -> str:                   #Вывод списка документов 
    pass

def KOFNTResultsComps() -> str:                      #Вывод списка результатов сорев
    pass



df_base = pd.read_excel("D:\Git\TT\PingPong-Bot\data\База.xlsx")
df_match = pd.read_excel("D:\Git\TT\PingPong-Bot\data\Список матчей.xlsx")

print(df_match['Имя 1'].values[1])