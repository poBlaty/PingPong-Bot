import pandas as pd


def LastComp(name: str) -> list:  # Результаты встреч на последних сыгранных соревах
    df_list_match = pd.read_excel("../data\Список матчей.xlsx")

    sets = ['Партия 1 1', 'Партия 1 2', 'Партия 2 1', 'Партия 2 2', 'Партия 3 1', 'Партия 3 2', 'Партия 4 1',
            'Партия 4 2', 'Партия 5 1', 'Партия 5 2', 'Партия 6 1', 'Партия 6 2', 'Партия 7 1', 'Партия 7 2']
    compName = []
    compIndex = []
    result = []
    l = len(df_list_match["Имя 1"])

    for i in range(l):
        if df_list_match['Название соревнований'].values[i] not in compName:
            compIndex.append(i)
        compName.append(df_list_match['Название соревнований'].values[i])
    compName = list(set(compName))
    lastComp = ''

    for i in range(l - 1, -1, -1):
        if str(df_list_match["Имя 1"].values[i]).lower().title() == name or str(
                df_list_match["Имя 2"].values[i]).lower().title() == name:
            lastComp = df_list_match["Название соревнований"].values[i]
            break
    result.append(lastComp)
    for i in range(l - 1, -1, -1):
        point = '('
        if int(str(df_list_match['Общий счет'].values[i]).split(':')[0]) > int(
                str(df_list_match['Общий счет'].values[i]).split(':')[1]):
            for j in range(0, len(sets), 2):
                if df_list_match[sets[j]].values[i] > df_list_match[sets[j + 1]].values[i]:
                    try:
                        point += str(int(df_list_match[sets[j + 1]].values[i])) + ', '
                    except:
                        continue
                else:
                    try:
                        point += str(-1 * int(df_list_match[sets[j]].values[i])) + ', '
                    except:
                        continue
        if int(str(df_list_match['Общий счет'].values[i]).split(':')[0]) < int(
                str(df_list_match['Общий счет'].values[i]).split(':')[1]):
            for j in range(0, len(sets), 2):
                if df_list_match[sets[j]].values[i] > df_list_match[sets[j + 1]].values[i]:
                    try:
                        point += str(-1 * int(df_list_match[sets[j + 1]].values[i])) + ', '
                    except:
                        continue
                else:
                    try:
                        point += str(int(df_list_match[sets[j]].values[i])) + ', '
                    except:
                        continue
        a = 0
        if df_list_match["Название соревнований"].values[i] != lastComp:
            i -= l - compIndex[a]
            a += 1
        point = point[:-2] + ')'

        if str(df_list_match["Имя 1"].values[i]).lower().title() == name or str(
                df_list_match["Имя 2"].values[i]).lower().title() == name:
            result.append(
                f'{str(df_list_match["Имя 1"].values[i]).lower().title()} {df_list_match["Общий счет"].values[i]} {str(df_list_match["Имя 2"].values[i]).lower().title()} {point}')

    return result
