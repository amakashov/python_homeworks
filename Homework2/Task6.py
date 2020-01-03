# Четвёртая необязательная задача

def makeChampTable(seasonResults):
    teams = {}  #   Ок, пустой словарик для команд
    for results in seasonResults.values():      #   По турам
        for fixture, score in results.items():  #   По матчам
            homeTeam, awayTeam = fixture.split("-") #   Выдёргиваем названия оманд
            homeTeam, awayTeam = str.strip(homeTeam), str.strip(awayTeam)   #   убираем лишние пробелы
            if homeTeam not in teams:   #   Если домашний команды ещё нет в словаре, добавим пустую
                teams[homeTeam] = {"Played" : 0 , "Wins" : 0, "Draw":0, "Loss":0, "Points":0, "F":0, "A":0, "GD":0}
            if awayTeam not in teams:   #   аналогично для гостевой
                teams[awayTeam] = {"Played" : 0 , "Wins" : 0, "Draw":0, "Loss":0, "Points":0, "F":0, "A":0, "GD":0}
            homeScore,awayScore = score.split("-")  #   Разбираем счёт
            homeScore,awayScore = int(homeScore),int(awayScore) 
            if (homeScore==awayScore):      # ничья
                teams[homeTeam]["Draws"] +=1
                teams[awayTeam]["Draws"] +=1
            elif (homeScore< awayScore):    #   победа гостей
                teams[homeTeam]["Loss"] +=1
                teams[awayTeam]["Wins"] +=1
            else:                           #   домашняя победа
                teams[homeTeam]["Wins"] +=1
                teams[awayTeam]["Loss"] +=1
            teams[homeTeam]["F"] += homeScore   # можно было бы просто разницу считать, но нет
            teams[awayTeam]["A"] += homeScore   # вдруг потом по забитым сортировать
            teams[homeTeam]["A"] += awayScore
            teams[awayTeam]["F"] += awayScore
    for team,played in teams.items():           # Всё, считаем общее число матчей, очков и разницу
        teams[team]["Played"] = played["Wins"] + played["Draw"]+played["Loss"]
        teams[team]["Points"] = 3* played["Wins"] + played["Draw"]
        teams[team]["GD"] = played["F"] - played["A"]
        # и сортируем (подглядел на stackoverflow про tuple и минус для порядка сортировки)
    teams = {team:result for team,result in sorted(teams.items(), key = lambda item : (-item[1]["Points"], -item[1]["GD"], item[0]))}    
    return teams

def printChampTable(teams):     #   Просто печать таблички
    print('{}{}{}'.format("|", "="*(49+6),"|")) 
    print('|{:^14}|{:^6}|{:^6}|{:^6}|{:^6}|{:^5}|{:^6}|'.format("Team", 'Played', 'Wins', 'Draw', 'Loss', 'GD', 'Points'))
    print('{}{}{}'.format("|", "="*(49+6),"|"))
    for team,stats in teams.items():
        print('|{:^14}|{:^6}|{:^6}|{:^6}|{:^6}|{:^5}|{:^6}|'
              .format(team, stats['Played'], stats['Wins'], stats['Draw'], stats['Loss'], stats['GD'], stats['Points']))
    print('{}{}{}'.format("|", "="*(49+6),"|"))




results = {1:
           {
               'Spartak - Dynamo': "3 - 1",
               'Arsenal - Lokomotiv': "4 - 0",
               'Zenit - Krasnodar': "1 - 2",
               'CSKA - Rubin': "1 - 2"
           },
           2: {
               'Lokomotiv - Zenit': "3 - 2",
               'CSKA  - Spartak': "4 - 0",
               'Dynamo - Krasnodar': "1 - 2",
               'Arsenal - Rubin': "1 - 2"
           }
          }

teams = makeChampTable(results)
printChampTable(teams)