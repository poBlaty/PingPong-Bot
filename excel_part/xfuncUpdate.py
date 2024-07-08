import pandas as pd
import numpy as np


def RaitingFileUpdate(link: str):  # Обновление файла "Рейтинг"
    df_raiting_new_m = pd.read_excel(link)
    df_base = pd.read_excel("data/Рейтинг.xlsx")

    month = df_raiting_new_m['Unnamed: 5'].values[0]
    l = len(df_raiting_new_m['Фамилия Имя'])
    b = len(df_base['Фамилия'])
    three = []

    if l != b:
        one = df_raiting_new_m['Фамилия Имя'].to_list()
        two = []
        for i in range(b):
            two.append(f"{df_base['Фамилия'][i]} {df_base['Имя'][i]}")
        three = list(set(one) - set(two))

        for i in range(len(three)):
            df_base.at[b + i, 'Фамилия'] = three[i].split(' ')[0]
            df_base.at[b + i, 'Имя'] = three[i].split(' ')[1]
            for j in range(l):
                if df_raiting_new_m['Фамилия Имя'].values[j] == three[i]:
                    df_base.at[b + i, month] = df_raiting_new_m['Рейтинг'].values[j]

    for i in range(l):
        surename = df_raiting_new_m['Фамилия Имя'].values[i].split(' ')[0]
        surename = surename.replace(' ', '')
        name = df_raiting_new_m['Фамилия Имя'].values[i].split(' ')[1]
        name = name.replace(' ', '')
        raiting = df_raiting_new_m['Рейтинг'].values[i]

        for j in range(b - len(three)):
            if f"{surename} {name}" == f"{df_base['Фамилия'][j]} {df_base['Имя'][j]}":
                df_base.at[j, month] = raiting
                continue

    df_base.to_excel("data/Рейтинг.xlsx", index=False)


def RaitingKOFNTUpdate(link: str):  # Обновление файла "База" КОФНТ рейтинг

    df_base = pd.read_excel("data/База.xlsx")
    df_raiting_new_m = pd.read_excel(link)
    l = len(df_raiting_new_m['Фамилия Имя'])
    b = len(df_base['Фамилия'])
    three = []

    if l != b:
        one = df_raiting_new_m['Фамилия Имя'].to_list()
        two = []
        for i in range(b):
            two.append(f"{df_base['Фамилия'][i]} {df_base['Имя'][i]}")
        three = list(set(one) - set(two))
        for i in range(len(three)):
            df_base.at[b + i, 'Фамилия'] = three[i].split(' ')[0]
            df_base.at[b + i, 'Имя'] = three[i].split(' ')[1]
            for j in range(l):
                if df_raiting_new_m['Фамилия Имя'].values[j] == three[i]:
                    df_base.at[b + i, "Дата рождения"] = \
                    str(df_raiting_new_m['Дата рождения'].values[j]).split('T')[0].split(' ')[0]
                    df_base.at[b + i, "Рейтинг КОФНТ"] = df_raiting_new_m['Рейтинг'].values[j]
                    df_base.at[b + i, "Город"] = df_raiting_new_m["Город"].values[j]

    for i in range(l):
        surename = df_raiting_new_m['Фамилия Имя'].values[i].split(' ')[0]
        surename = surename.replace(' ', '')
        name = df_raiting_new_m['Фамилия Имя'].values[i].split(' ')[1]
        name = name.replace(' ', '')
        raiting = df_raiting_new_m['Рейтинг'].values[i]

        for j in range(b - len(three)):
            if f"{surename} {name}" == f"{df_base['Фамилия'][j]} {df_base['Имя'][j]}":
                df_base.at[j, "Рейтинг КОФНТ"] = raiting
                continue

    df_base.to_excel("../data/База.xlsx", index=False)


def RaitingFNTRUpdate(link: str):  # Обновление файла "База" ФНТР рейтинг

    df_base = pd.read_excel("data/База.xlsx")
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

        for j in range(b - len(three)):
            if f"{surename} {name}" == f"{df_base['Фамилия'][j]} {df_base['Имя'][j]}":
                df_base.at[j, "Рейтинг ФНТР"] = raiting
                continue
    df_base.to_excel("data/База.xlsx", index=False)


def CompUpdate(link: str):  # Обновление файла "База" разряд и город

    df_base = pd.read_excel("data/База.xlsx")
    df_comp_result = pd.ExcelFile(link)
    sheet1 = df_comp_result.parse('АлфСписокМ')
    sheet2 = df_comp_result.parse('АлфСписокЖ')

    b = len(df_base['Фамилия'])
    l1 = len(sheet1.iloc[0, 0])
    l2 = len(sheet2.iloc[0, 0])

    players1 = []
    for i in range(l1):
        if sheet1['Unnamed: 1'].values[i] not in ['', 'ФИО']:
            players1.append(str(sheet1['Unnamed: 1'].values[i]))
    players1 = [x for x in players1 if x != 'nan']

    players2 = []
    for i in range(l2):
        if sheet1['Unnamed: 1'].values[i] not in ['', 'ФИО']:
            players2.append(str(sheet2['Unnamed: 1'].values[i]))
    players2 = [x for x in players2 if x != 'nan']

    category1 = []
    for i in range(len(players1)):
        category1.append(str(sheet1['Unnamed: 4'].values[i + 5]))

    city1 = []
    for i in range(len(players1)):
        city1.append(str(sheet1['Unnamed: 8'].values[i + 5]))

    category2 = []
    for i in range(len(players2)):
        category2.append(str(sheet2['Unnamed: 4'].values[i + 5]))

    city2 = []
    for i in range(len(players2)):
        city2.append(str(sheet2['Unnamed: 8'].values[i + 5]))

    players = players1 + players2
    category = category1 + category2
    city = city1 + city2

    for i in range(len(players)):
        for j in range(b):
            if f"{df_base['Фамилия'][j]} {df_base['Имя'][j]}".lower().strip() == str(players[i]).lower().strip():
                df_base.at[j, 'Разряд'] = category[i]
                df_base.at[j, 'Город'] = city[i]

    df_base.to_excel("data/База.xlsx", index=False)


def PlayersPlaceRaitingOnComp(
        link: str) -> list:  # Участники соревнования, их места, их рейтинг на момент проведения из файла с соревами
    df_comp_result = pd.ExcelFile(link)
    sheet1 = df_comp_result.parse('АлфСписокМ')
    sheet2 = df_comp_result.parse('АлфСписокЖ')

    sheet_names = df_comp_result.sheet_names

    l1 = len(sheet1.iloc[0, 0])
    l2 = len(sheet2.iloc[0, 0])

    players1 = []
    for i in range(l1):
        if sheet1['Unnamed: 1'].values[i] not in ['', 'ФИО']:
            players1.append(str(sheet1['Unnamed: 1'].values[i]))
    players1 = [x for x in players1 if x != 'nan']

    players2 = []
    for i in range(l2):
        if sheet1['Unnamed: 1'].values[i] not in ['', 'ФИО']:
            players2.append(str(sheet2['Unnamed: 1'].values[i]))
    players2 = [x for x in players2 if x != 'nan']
    players = players1 + players2

    playableSheets = []
    for i in sheet_names:
        sheet = df_comp_result.parse(i)
        try:
            if sheet['Unnamed: 10'].values[0] in [8, 16, 24, 32, 48]:
                playableSheets.append(i)
        except:
            continue

    results = []
    for i in playableSheets:
        sheet = df_comp_result.parse(i)
        places = sheet['Unnamed: 10'].values[0]

        for j in range(places):
            results.append([sheet["Место"].values[j + 3], str(sheet["Фамилия, имя"].values[j + 3]).strip(),
                            sheet["Рейтинг"].values[j + 3]])

    results = [x for x in results if x[1] not in ['x', 'х', 'nan']]

    return results


def CompInfo(link: str) -> list:  # Информация о турнире (Название, город проведения, дата)
    df_comp_result = pd.ExcelFile(link)
    sheet = df_comp_result.parse('Титульный')

    info = []

    for i in range(len(sheet['Unnamed: 0'])):
        if sheet['Unnamed: 0'].values[i] != '':
            info.append(str(sheet['Unnamed: 0'].values[i]))

    info = [x for x in info if x != 'nan']
    info = [f"{info[0]} {info[1]} {info[2]}", info[3], info[4]]
    return info


def ListMatchUpdate(link: str):  # Обновление файла Список матчей
    df_comp_result = pd.ExcelFile(link)
    df_list_match = pd.read_excel("data/Список матчей.xlsx")
    sheet_names = df_comp_result.sheet_names

    playableSheets = []

    data = CompInfo(link)[-1]

    for i in sheet_names:
        sheet = df_comp_result.parse(i)
        try:
            if sheet['Unnamed: 10'].values[0] in [8, 16, 24, 32, 48]:
                playableSheets.append(i)
        except:
            continue

    value = []
    for i in playableSheets:
        sheet = df_comp_result.parse(i)

        v = -1
        for j in range(len(sheet['Unnamed: 0']) - 1):
            try:
                v = max(v, int(sheet['Unnamed: 0'].values[j + 1]))
            except:
                continue
        value.append([v, i])

    for i in range(len(value)):
        sheet = df_comp_result.parse(value[i][1])

        matches = [j for j in range(1, value[i][0] + 1)]
        stages = []
        players = []
        score = []

        for j in range(1, len(sheet['Unnamed: 0'])):
            if sheet['Unnamed: 0'].values[j] in matches:
                scoresheet = sheet.iloc[j, 10:24]
                stages.append(sheet['Unnamed: 1'].values[j])
                players.append(
                    [sheet['День/Время/Стол'].values[j], sheet['Unnamed: 24'].values[j], sheet['Unnamed: 25'].values[j],
                     sheet['День/Время/Стол'].values[j + 1]])
                score.append(
                    f"{scoresheet['Unnamed: 10']}, {scoresheet['с какого места начинается сетка ↓']}, {scoresheet['Unnamed: 12']}, {scoresheet['Unnamed: 13']}, {scoresheet['Unnamed: 14']}, {scoresheet['Unnamed: 15']}, {scoresheet['Unnamed: 16']}, {scoresheet['Unnamed: 17']}, {scoresheet['Unnamed: 18']}, {scoresheet['Unnamed: 19']}, {scoresheet['2']}, {scoresheet['Фамилия Имя']}, {scoresheet['Unnamed: 22']}, {scoresheet['Unnamed: 23']}")

        for j in range(len(score)):
            score[i] = str(score[i])

        for k in range(len(matches)):
            matches[k] = [k + 1, stages[k], players[k][0], players[k][1], players[k][2], score[k], players[k][3]]

        if pd.isnull(matches).any():
            continue

        for j in range(len(matches)):
            for k in range(len(matches[j])):
                matches[j][k] = str(matches[j][k]).strip()

        matches.insert(0, CompInfo(link)[0])

        matchesFinal = []
        for j in range(1, len(matches)):
            if matches[j][2] == 'x' or matches[j][2] == 'х' or matches[j][-1] == 'x' or matches[j][-1] == 'х' or int(
                    matches[j][3]) + int(matches[j][4]) < 3:
                continue
            else:
                matchesFinal.append(matches[j])

        sets = ['Партия 1 1', 'Партия 1 2', 'Партия 2 1', 'Партия 2 2', 'Партия 3 1', 'Партия 3 2', 'Партия 4 1',
                'Партия 4 2', 'Партия 5 1', 'Партия 5 2', 'Партия 6 1', 'Партия 6 2', 'Партия 7 1', 'Партия 7 2']

        l = len(df_list_match['Имя 1'])

        for j in range(1, len(matchesFinal)):
            df_list_match.at[l + j, 'Стадия'] = matchesFinal[j][1]
            df_list_match.at[l + j, 'Имя 1'] = matchesFinal[j][2]
            df_list_match.at[l + j, 'Имя 2'] = matchesFinal[j][-1]
            df_list_match.at[l + j, 'Название соревнований'] = matches[0]
            for k in range(int(sheet['Unnamed: 10'].values[0])+48):
                if sheet["Фамилия, имя"].values[k] == matchesFinal[j][2]:
                    df_list_match.at[l + j, 'Рейтинг 1'] = sheet["Рейтинг"].values[k]
                if sheet["Фамилия, имя"].values[k] == matchesFinal[j][-1]:
                    df_list_match.at[l + j, 'Рейтинг 2'] = sheet["Рейтинг"].values[k]
            points = matchesFinal[j][5].split(', ')
            df_list_match.at[l + j, 'Дата'] = data

            for k in sets:
                df_list_match.at[l + j, k] = points[sets.index(k)]
            df_list_match.at[l + j, 'Общий счет'] = f"{matchesFinal[j][3]}:{matchesFinal[j][4]}"

        df_list_match.to_excel("data/Список матчей.xlsx", index=False)
