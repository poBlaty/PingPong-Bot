import pandas as pd

def LastComp(name: str) -> list:                             #Результаты встреч на последних сыгранных соревах
    df_list_match = pd.read_excel("data/Список матчей.xlsx")

    sets = ['Партия 1 1', 'Партия 1 2', 'Партия 2 1', 'Партия 2 2', 'Партия 3 1', 'Партия 3 2', 'Партия 4 1', 'Партия 4 2', 'Партия 5 1', 'Партия 5 2', 'Партия 6 1', 'Партия 6 2', 'Партия 7 1', 'Партия 7 2']
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

    for i in range(l-1, -1, -1):
        if str(df_list_match["Имя 1"].values[i]).lower().title() == name or str(df_list_match["Имя 2"].values[i]).lower().title() == name: 
            lastComp = df_list_match["Название соревнований"].values[i]
            break
    result.append(lastComp)
    for i in range(l-1, -1, -1):
        point = '('
        if int(str(df_list_match['Общий счет'].values[i]).split(':')[0]) > int(str(df_list_match['Общий счет'].values[i]).split(':')[1]):
            for j in range(0, len(sets), 2):
                if df_list_match[sets[j]].values[i] > df_list_match[sets[j+1]].values[i]:
                    try:
                        point += str(int(df_list_match[sets[j+1]].values[i])) + ', '
                    except:
                        continue
                else:
                    try:
                        point += str(-1*int(df_list_match[sets[j]].values[i])) + ', '
                    except:
                        continue
        if int(str(df_list_match['Общий счет'].values[i]).split(':')[0]) < int(str(df_list_match['Общий счет'].values[i]).split(':')[1]):
            for j in range(0, len(sets), 2):
                if df_list_match[sets[j]].values[i] > df_list_match[sets[j+1]].values[i]:
                    try:
                        point += str(-1*int(df_list_match[sets[j+1]].values[i])) + ', '
                    except:
                        continue
                else:
                    try:
                        point += str(int(df_list_match[sets[j]].values[i])) + ', '
                    except:
                        continue
        a = 0
        if df_list_match["Название соревнований"].values[i] != lastComp:
            i-= l-compIndex[a]
            a+=1
        point = point[:-2]+ ')'
        
        if str(df_list_match["Имя 1"].values[i]).lower().title() == name or str(df_list_match["Имя 2"].values[i]).lower().title() == name:
            result.append([str(df_list_match["Имя 1"].values[i]).lower().title(), df_list_match["Общий счет"].values[i], str(df_list_match["Имя 2"].values[i]).lower().title(), point])

    return result

def BestWins(name: str) -> list:                            #Лучшие победы
    df_list_match = pd.read_excel("data\Список матчей.xlsx")

    sets = ['Партия 1 1', 'Партия 1 2', 'Партия 2 1', 'Партия 2 2', 'Партия 3 1', 'Партия 3 2', 'Партия 4 1', 'Партия 4 2', 'Партия 5 1', 'Партия 5 2', 'Партия 6 1', 'Партия 6 2', 'Партия 7 1', 'Партия 7 2']
    result = []

    l = len(df_list_match["Имя 1"])
    
    for i in range(l-1, -1, -1):
        point = '('
        winner = ''
        loser = ''
        if int(str(df_list_match['Общий счет'].values[i]).split(':')[0]) > int(str(df_list_match['Общий счет'].values[i]).split(':')[1]):
            winner = str(df_list_match["Имя 1"].values[i]).lower().title()
            loser = str(df_list_match["Имя 2"].values[i]).lower().title()
            for j in range(0, len(sets), 2):
                try:
                    if int(df_list_match[sets[j]].values[i]) > int(df_list_match[sets[j+1]].values[i]):
                        try:
                            point += str(int(df_list_match[sets[j+1]].values[i])) + ', '
                        except:
                            continue
                    else:
                        try:
                            point += str(-1*int(df_list_match[sets[j]].values[i])) + ', '
                        except:
                            continue
                except:
                    continue
        if int(str(df_list_match['Общий счет'].values[i]).split(':')[0]) < int(str(df_list_match['Общий счет'].values[i]).split(':')[1]):
            winner = str(df_list_match["Имя 2"].values[i]).lower().title()
            loser = str(df_list_match["Имя 1"].values[i]).lower().title()
            for j in range(0, len(sets), 2):
                try:
                    if int(df_list_match[sets[j]].values[i]) > int(df_list_match[sets[j+1]].values[i]):
                        try:
                            point += str(-1*int(df_list_match[sets[j+1]].values[i])) + ', '
                        except:
                            continue
                    else:
                        try:
                            point += str(int(df_list_match[sets[j]].values[i])) + ', '
                        except:
                            continue
                except:
                    continue
        point = point[:-2]+ ')'

        if (str(df_list_match["Имя 1"].values[i]).lower().title() == name or str(df_list_match["Имя 2"].values[i]).lower().title() == name) and winner == name:
            result.append([df_list_match["Название соревнований"].values[i] , str(df_list_match["Имя 1"].values[i]).lower().title(), int(df_list_match["Рейтинг 1"].values[i]), df_list_match["Общий счет"].values[i], str(df_list_match["Имя 2"].values[i]).lower().title(), int(df_list_match["Рейтинг 2"].values[i]), point])

    diff = []
    for j in range(len(result)):
        if int(str(result[j][3]).split(':')[0]) > int(str(result[j][3]).split(':')[1]):
            winner = result[j][1]
            loser = result[j][-3]
        else:
            winner = result[j][-3]
            loser = result[j][1]
        diff.append(result[j][result[j].index(winner)+1] - result[j][result[j].index(loser)+1])

    x = zip(result, diff)
    xs = sorted(x, key=lambda k: k[1], reverse=False)
    result = [x[0] for x in xs]

    return result[:5]

def HeadToHead(fullname1: str, fullname2: str):              #Статистика личных встреч между двумя игроками
    fullname = [fullname1, fullname2]
    df_list_match = pd.read_excel("data\Список матчей.xlsx")

    sets = ['Партия 1 1', 'Партия 1 2', 'Партия 2 1', 'Партия 2 2', 'Партия 3 1', 'Партия 3 2', 'Партия 4 1', 'Партия 4 2', 'Партия 5 1', 'Партия 5 2', 'Партия 6 1', 'Партия 6 2', 'Партия 7 1', 'Партия 7 2']
    result = []

    l = len(df_list_match["Имя 1"])

    for i in range(l-1, -1, -1):
        point = '('
        winner = ''
        loser = ''
        if int(str(df_list_match['Общий счет'].values[i]).split(':')[0]) > int(str(df_list_match['Общий счет'].values[i]).split(':')[1]):
            winner = str(df_list_match["Имя 1"].values[i]).lower().title()
            loser = str(df_list_match["Имя 2"].values[i]).lower().title()
            for j in range(0, len(sets), 2):
                try:
                    if int(df_list_match[sets[j]].values[i]) > int(df_list_match[sets[j+1]].values[i]):
                        try:
                            point += str(int(df_list_match[sets[j+1]].values[i])) + ', '
                        except:
                            continue
                    else:
                        try:
                            point += str(-1*int(df_list_match[sets[j]].values[i])) + ', '
                        except:
                            continue
                except:
                    continue
        if int(str(df_list_match['Общий счет'].values[i]).split(':')[0]) < int(str(df_list_match['Общий счет'].values[i]).split(':')[1]):
            winner = str(df_list_match["Имя 2"].values[i]).lower().title()
            loser = str(df_list_match["Имя 1"].values[i]).lower().title()
            for j in range(0, len(sets), 2):
                try:
                    if int(df_list_match[sets[j]].values[i]) > int(df_list_match[sets[j+1]].values[i]):
                        try:
                            point += str(-1*int(df_list_match[sets[j+1]].values[i])) + ', '
                        except:
                            continue
                    else:
                        try:
                            point += str(int(df_list_match[sets[j]].values[i])) + ', '
                        except:
                            continue
                except:
                    continue
        point = point[:-2]+ ')'

        if (str(df_list_match["Имя 1"].values[i]).lower().title() in fullname and str(df_list_match["Имя 2"].values[i]).lower().title() in fullname) and winner:
            result.append([df_list_match["Название соревнований"].values[i] , str(df_list_match["Имя 1"].values[i]).lower().title(), int(df_list_match["Рейтинг 1"].values[i]), df_list_match["Общий счет"].values[i], str(df_list_match["Имя 2"].values[i]).lower().title(), int(df_list_match["Рейтинг 2"].values[i]), point])
    if len(result):
        return 0
