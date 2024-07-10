import pandas as pd
import xmain as xm

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

def BestWins(name: str, value: int) -> list:                            #Лучшие победы
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

    value = min(len(result)-1, value)

    return result[:value]

def HeadToHead(fullname1: str, fullname2: str) -> list:              #Статистика личных встреч между двумя игроками
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
    if len(result) == 0:
        return 0
    return result

def CompsValueYear(year: int, name: str) -> int:             #Количество сорев (На вход: (год, имя)) если без них, то 0 и ''
    df_list_match = pd.read_excel("data\Список матчей.xlsx")
    l = len(df_list_match["Имя 1"])
    result = []

    if year == 0 and name == '':
        for i in range(l-1, -1, -1):
            result.append(df_list_match["Название соревнований"].values[i])

    if year != 0 and name == '':
        for i in range(l-1, -1, -1):
            if int(str(df_list_match["Дата"].values[i]).split(' ')[-2]) == year:
                result.append(df_list_match["Название соревнований"].values[i])
    
    if year == 0 and name == '':
        for i in range(l-1, -1, -1):
            if str(df_list_match['Имя 1'].values[i]).lower().title() == name or str(df_list_match['Имя 2'].values[i]).lower().title() == name:
                result.append(df_list_match["Название соревнований"].values[i])

    if year != 0 and name != '':
        for i in range(l-1, -1, -1):
            if (str(df_list_match['Имя 1'].values[i]).lower().title() == name or str(df_list_match['Имя 2'].values[i]).lower().title() == name) and int(str(df_list_match["Дата"].values[i]).split(' ')[-2]) == year:
                result.append(df_list_match["Название соревнований"].values[i])

    result.append(df_list_match["Название соревнований"].values[i])
    
    result = len(list(set(result)))

    return result

def MatchValueYear(year: int, name: str) -> int:             #Количество матчей (На вход: (год, имя)) если без них, то 0 и ''
    df_list_match = pd.read_excel("data\Список матчей.xlsx")
    l = len(df_list_match["Имя 1"])
    
    sum = 0

    if year == 0 and name == '':
        return l

    if year != 0 and name == '':
        for i in range(l-1, -1, -1):
            if int(str(df_list_match["Дата"].values[i]).split(' ')[-2]) == year:
                sum += 1
    
    if year == 0 and name != '':
        for i in range(l-1, -1, -1):
            if str(df_list_match['Имя 1'].values[i]).lower().title() == name or str(df_list_match['Имя 2'].values[i]).lower().title() == name:
                sum += 1

    if year != 0 and name != '':
        for i in range(l-1, -1, -1):
            if (str(df_list_match['Имя 1'].values[i]).lower().title() == name or str(df_list_match['Имя 2'].values[i]).lower().title() == name) and int(str(df_list_match["Дата"].values[i]).split(' ')[-2]) == year:
                sum += 1

    return sum

def SetsValueYear(year: int, name: str) -> int:             #Количество партий (На вход: (год, имя)) если без них, то 0 и ''
    df_list_match = pd.read_excel("data\Список матчей.xlsx")
    l = len(df_list_match["Имя 1"])
    sum = 0

    if year == 0 and name == '':
        for i in range(l-1, -1, -1):
            sum += int(str(df_list_match["Общий счет"].values[i]).split(':')[0]) + int(str(df_list_match["Общий счет"].values[i]).split(':')[1])

    if year != 0 and name == '':
        for i in range(l-1, -1, -1):
            if int(str(df_list_match["Дата"].values[i]).split(' ')[-2]) == year:
                sum += int(str(df_list_match["Общий счет"].values[i]).split(':')[0]) + int(str(df_list_match["Общий счет"].values[i]).split(':')[1])
    
    if year == 0 and name != '':
        for i in range(l-1, -1, -1):
            if str(df_list_match['Имя 1'].values[i]).lower().title() == name or str(df_list_match['Имя 2'].values[i]).lower().title() == name:
                sum += int(str(df_list_match["Общий счет"].values[i]).split(':')[0]) + int(str(df_list_match["Общий счет"].values[i]).split(':')[1])

    if year != 0 and name != '':
        for i in range(l-1, -1, -1):
            if (str(df_list_match['Имя 1'].values[i]).lower().title() == name or str(df_list_match['Имя 2'].values[i]).lower().title() == name) and int(str(df_list_match["Дата"].values[i]).split(' ')[-2]) == year:
                sum += int(str(df_list_match["Общий счет"].values[i]).split(':')[0]) + int(str(df_list_match["Общий счет"].values[i]).split(':')[1])

    return sum

def PointsValueYear(year: int, name: str) -> int:           #Количество очков (На вход: (год, имя)) если без них, то 0 и ''
    df_list_match = pd.read_excel("data\Список матчей.xlsx")
    l = len(df_list_match["Имя 1"])
    sets = ['Партия 1 1', 'Партия 1 2', 'Партия 2 1', 'Партия 2 2', 'Партия 3 1', 'Партия 3 2', 'Партия 4 1', 'Партия 4 2', 'Партия 5 1', 'Партия 5 2', 'Партия 6 1', 'Партия 6 2', 'Партия 7 1', 'Партия 7 2']

    sum = 0

    if year == 0 and name == '':
        for i in range(l-1, -1, -1):
            for j in sets:
                try:
                    sum += int(df_list_match[j].values[i])
                except:
                    continue

    if year != 0 and name == '':
        for i in range(l-1, -1, -1):
            if int(str(df_list_match["Дата"].values[i]).split(' ')[-2]) == year:
                for j in sets:
                    try:
                        sum += int(df_list_match[j].values[i])
                    except:
                        continue
    
    if year == 0 and name != '':
        for i in range(l-1, -1, -1):
            if str(df_list_match['Имя 1'].values[i]).lower().title() == name or str(df_list_match['Имя 2'].values[i]).lower().title() == name:
                for j in sets:
                    try:
                        sum += int(df_list_match[j].values[i])
                    except:
                        continue

    if year != 0 and name != '':
        for i in range(l-1, -1, -1):
            if (str(df_list_match['Имя 1'].values[i]).lower().title() == name or str(df_list_match['Имя 2'].values[i]).lower().title() == name) and int(str(df_list_match["Дата"].values[i]).split(' ')[-2]) == year:
                for j in sets:
                    try:
                        sum += int(df_list_match[j].values[i])
                    except:
                        continue

    return sum

def WinMatchValueYear(year: int, name: str) -> int:             #Количество выигранных матчей (На вход: (год, имя)) если без года, то 0
    df_list_match = pd.read_excel("data\Список матчей.xlsx")
    l = len(df_list_match["Имя 1"])

    sum = 0

    if year == 0:
        for i in range(l-1, -1, -1):
            winner = ''
            if int(str(df_list_match['Общий счет'].values[i]).split(':')[0]) > int(str(df_list_match['Общий счет'].values[i]).split(':')[1]):
                winner = str(df_list_match["Имя 1"].values[i]).lower().title()
            if int(str(df_list_match['Общий счет'].values[i]).split(':')[0]) < int(str(df_list_match['Общий счет'].values[i]).split(':')[1]):
                winner = str(df_list_match["Имя 2"].values[i]).lower().title()

            if winner == name:
                sum += 1

    else:
        for i in range(l-1, -1, -1):
            winner = ''
            if int(str(df_list_match['Общий счет'].values[i]).split(':')[0]) > int(str(df_list_match['Общий счет'].values[i]).split(':')[1]):
                winner = str(df_list_match["Имя 1"].values[i]).lower().title()
            if int(str(df_list_match['Общий счет'].values[i]).split(':')[0]) < int(str(df_list_match['Общий счет'].values[i]).split(':')[1]):
                winner = str(df_list_match["Имя 2"].values[i]).lower().title()

            if int(str(df_list_match["Дата"].values[i]).split(' ')[-2]) == year and winner == name:
                sum += 1

    return sum

def WinSetsValueYear(year: int, name: str) -> int:             #Количество выигранных партий (На вход: (год, имя)) если без года, то 0
    df_list_match = pd.read_excel("data\Список матчей.xlsx")
    l = len(df_list_match["Имя 1"])
    sum = 0
    
    if year == 0:
        for i in range(l-1, -1, -1):
            if str(df_list_match["Имя 1"].values[i]).lower().title() == name:
                sum += int(str(df_list_match["Общий счет"].values[i]).split(':')[0])
            if str(df_list_match["Имя 2"].values[i]).lower().title() == name:
                sum += int(str(df_list_match["Общий счет"].values[i]).split(':')[1])

    else:
        for i in range(l-1, -1, -1):
            if int(str(df_list_match["Дата"].values[i]).split(' ')[-2]) == year:
                if str(df_list_match["Имя 1"].values[i]).lower().title() == name:
                    sum += int(str(df_list_match["Общий счет"].values[i]).split(':')[0])
                if str(df_list_match["Имя 2"].values[i]).lower().title() == name:
                    sum += int(str(df_list_match["Общий счет"].values[i]).split(':')[1])

    return sum

def WinPointsValueYear(year: int, name: str) -> int:           #Количество выигранных очков (На вход: (год, имя)) если без года, то 0
    df_list_match = pd.read_excel("data\Список матчей.xlsx")
    l = len(df_list_match["Имя 1"])
    sets = ['Партия 1 1', 'Партия 1 2', 'Партия 2 1', 'Партия 2 2', 'Партия 3 1', 'Партия 3 2', 'Партия 4 1', 'Партия 4 2', 'Партия 5 1', 'Партия 5 2', 'Партия 6 1', 'Партия 6 2', 'Партия 7 1', 'Партия 7 2']

    sum = 0

    if year == 0:
        for i in range(l-1, -1, -1):
            if str(df_list_match['Имя 1'].values[i]).lower().title() == name:
                for j in range(0, len(sets)+1, 2):
                    try:
                        sum += int(df_list_match[sets[j]].values[i])
                    except:
                        continue
            if str(df_list_match['Имя 2'].values[i]).lower().title() == name:
                for j in range(1, len(sets)+1, 2):
                    try:
                        sum += int(df_list_match[sets[j]].values[i])
                    except:
                        continue
    else:
        for i in range(l-1, -1, -1):
            if int(str(df_list_match["Дата"].values[i]).split(' ')[-2]) == year:
                if str(df_list_match['Имя 1'].values[i]).lower().title() == name:
                    for j in range(0, len(sets)+1, 2):
                        try:
                            sum += int(df_list_match[sets[j]].values[i])
                        except:
                            continue
                if str(df_list_match['Имя 2'].values[i]).lower().title() == name:
                    for j in range(1, len(sets)+1, 2):
                        try:
                            sum += int(df_list_match[sets[j]].values[i])
                        except:
                            continue

    return sum

def PlaceInRaitingKOFNT(name: str) -> int:          #НЕТЕСТИЛОСЬ Место игрока в рейтинге КОФНТ в последнем месяце
    df_raiting = pd.read_excel("data/Рейтинг.xlsx")

    l = len(df_raiting['Фамилия'])
    col = list(df_raiting)
    namesM = []
    raitingM = []
    namesW = []
    raitingW = []
    name = name.split(' ')

    for i in range(l-1):
        if xm.GenderBase(xm.GetIdByName(df_raiting['Фамилия'].values[i], df_raiting['Имя'].values[i])) == 'М':
            namesM.append(f"{df_raiting['Фамилия'].values[i]} {df_raiting['Имя'].values[i]}")
            raitingM.append(df_raiting[col[-1]].values[i])

    for i in range(l-1):
        if xm.GenderBase(xm.GetIdByName(df_raiting['Фамилия'].values[i], df_raiting['Имя'].values[i])) == 'Ж':
            namesM.append(f"{df_raiting['Фамилия'].values[i]} {df_raiting['Имя'].values[i]}")
            raitingM.append(df_raiting[col[-1]].values[i])

    if xm.GenderBase(xm.GetIdByName(name[0], name[1])) == 'М':
        x = zip(namesM, raitingM)
        xs = sorted(x, key=lambda k: k[1], reverse=True)
        resultM = [x[0] for x in xs]
        return resultM.index(name)+1

    if xm.GenderBase(xm.GetIdByName(name[0], name[1])) == 'М':
        x = zip(namesW, raitingW)
        xs = sorted(x, key=lambda k: k[1], reverse=True)
        resultW = [x[0] for x in xs]
        return resultW.index(name)+1
    
def PlaceAndRaitingOnYear(name: str) -> list:
    pass