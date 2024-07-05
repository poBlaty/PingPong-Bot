import pandas as pd

def RaitingFileUpdate():
    pass

def RaitingKOFNTUpdate(link:str):
    df_raiting_new_m = pd.read_excel(link)
    df_base = pd.read_excel("D:\Git\TT\PingPong-Bot\data\Рейтинг.xlsx")
    
    month = link.split("\\")[-1].split('.')[0]
    l = len(df_raiting_new_m['Фамилия Имя'])
    three = []

    if l != len(df_base['Фамилия']):
        one = df_raiting_new_m['Фамилия Имя'].to_list()
        two = []
        for i in range(len(df_base['Фамилия'])):
            two.append(f"{df_base['Фамилия'][i]} {df_base['Имя'][i]}")
        three = list(set(one)-set(two))
        
        for i in range(len(three)):
            df_base.at[l, 'Фамилия'] = three[i].split(' ')[0]
            df_base.at[l, 'Имя'] = three[i].split(' ')[1]
            for j in range(l):
                if df_raiting_new_m['Фамилия Имя'].values[j] == three[i]:
                    df_base.at[l, month] = df_raiting_new_m['Рейтинг'].values[j]
    df_base.to_excel("D:\Git\TT\PingPong-Bot\data\Рейтинг.xlsx", index=False)

    for i in range(l):
        surename = df_raiting_new_m['Фамилия Имя'].values[i].split(' ')[0]
        name = df_raiting_new_m['Фамилия Имя'].values[i].split(' ')[1]
        raiting = df_raiting_new_m['Рейтинг'].values[i]
        
        for j in range(len(df_base['Фамилия'])-len(three)):
            if f"{surename} {name}" == f"{df_base['Фамилия'][j]} {df_base['Имя'][j]}":
                df_base.at[j, month] = raiting
                continue

    df_base.to_excel("D:\Git\TT\PingPong-Bot\data\Рейтинг.xlsx", index=False)
        
def RaitingFNTRUpdate():
    pass

def RaitingRTTFUpdate():
    pass

def CategoryUpdate():
    pass

def CityUpdate():
    pass

RaitingKOFNTUpdate("D:\Git\TT\PingPong-Bot\data\garbage\Рейтинг\Мужчины\Август 2024.xlsm")