import pandas as pd

def RaitingFileUpdate(link:str):
    df_raiting_new_m = pd.read_excel(link)
    df_base = pd.read_excel("D:\Git\TT\PingPong-Bot\data\Рейтинг.xlsx")
    
    month = link.split("\\")[-1].split('.')[0]
    l = len(df_raiting_new_m['Фамилия Имя'])
    b = len(df_base['Фамилия'])
    three = []

    if l != b:
        one = df_raiting_new_m['Фамилия Имя'].to_list()
        two = []
        for i in range(b):
            two.append(f"{df_base['Фамилия'][i]} {df_base['Имя'][i]}")
        three = list(set(one)-set(two))
        
        for i in range(len(three)):
            df_base.at[b+i, 'Фамилия'] = three[i].split(' ')[0]
            df_base.at[b+i, 'Имя'] = three[i].split(' ')[1]
            for j in range(l):
                if df_raiting_new_m['Фамилия Имя'].values[j] == three[i]:
                    df_base.at[b+i, month] = df_raiting_new_m['Рейтинг'].values[j]

    for i in range(l):
        surename = df_raiting_new_m['Фамилия Имя'].values[i].split(' ')[0]
        surename = surename.replace(' ', '')
        name = df_raiting_new_m['Фамилия Имя'].values[i].split(' ')[1]
        name = name.replace(' ', '')
        raiting = df_raiting_new_m['Рейтинг'].values[i]
        
        for j in range(b-len(three)):
            if f"{surename} {name}" == f"{df_base['Фамилия'][j]} {df_base['Имя'][j]}":
                df_base.at[j, month] = raiting
                continue

    df_base.to_excel("D:\Git\TT\PingPong-Bot\data\Рейтинг.xlsx", index=False)

def RaitingKOFNTUpdate(link:str):
    
    df_base = pd.read_excel("D:\Git\TT\PingPong-Bot\data\База.xlsx")
    df_raiting_new_m = pd.read_excel(link)
    l = len(df_raiting_new_m['Фамилия Имя'])
    b = len(df_base['Фамилия'])
    three = []

    if l != b:
        one = df_raiting_new_m['Фамилия Имя'].to_list()
        two = []
        for i in range(b):
            two.append(f"{df_base['Фамилия'][i]} {df_base['Имя'][i]}")
        three = list(set(one)-set(two))
        for i in range(len(three)):
            df_base.at[b+i, 'Фамилия'] = three[i].split(' ')[0]
            df_base.at[b+i, 'Имя'] = three[i].split(' ')[1]
            for j in range(l):
                if df_raiting_new_m['Фамилия Имя'].values[j] == three[i]:
                    df_base.at[b+i, "Дата рождения"] = str(df_raiting_new_m['Дата рождения'].values[j]).split('T')[0].split(' ')[0]
                    df_base.at[b+i, "Рейтинг КОФНТ"] = df_raiting_new_m['Рейтинг'].values[j]
                    df_base.at[b+i, "Город"] = df_raiting_new_m["Город"].values[j]

    for i in range(l):
        surename = df_raiting_new_m['Фамилия Имя'].values[i].split(' ')[0]
        surename = surename.replace(' ', '')
        name = df_raiting_new_m['Фамилия Имя'].values[i].split(' ')[1]
        name = name.replace(' ', '')
        raiting = df_raiting_new_m['Рейтинг'].values[i]
        
        for j in range(b-len(three)):
            if f"{surename} {name}" == f"{df_base['Фамилия'][j]} {df_base['Имя'][j]}":
                df_base.at[j, "Рейтинг КОФНТ"] = raiting
                continue

    df_base.to_excel("D:\Git\TT\PingPong-Bot\data\База.xlsx", index=False)

def RaitingFNTRUpdate(link:str):

    df_base = pd.read_excel("D:\Git\TT\PingPong-Bot\data\База.xlsx")
    df_raiting_new_m = pd.read_excel(link)
    l = len(df_raiting_new_m['Фамилия Имя'])
    b = len(df_base['Фамилия'])
    three = []

    for i in range(l):
        surename = df_raiting_new_m['Фамилия Имя'].values[i].split(' ')[0]
        surename = surename.replace(' ', '')
        name = df_raiting_new_m['Фамилия Имя'].values[i].split(' ')[1]
        name = name.replace(' ', '')
        raiting = df_raiting_new_m['Рейтинг'].values[i]
        
        for j in range(b-len(three)):
            if f"{surename} {name}" == f"{df_base['Фамилия'][j]} {df_base['Имя'][j]}":
                df_base.at[j, "Рейтинг КОФНТ"] = raiting
                continue
def RaitingRTTFUpdate():
    pass


def CategoryUpdate():
    pass


def CityUpdate():
    pass


RaitingKOFNTUpdate("D:\Git\TT\PingPong-Bot\data\garbage\Рейтинг КОФНТ\Женщины\Июнь 2024.xlsm")
