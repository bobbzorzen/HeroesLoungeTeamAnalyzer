import requests
import pprint
from bs4 import BeautifulSoup

def getPickData(game):
    team1Picks = item.select(".row:nth-child(3) .col:nth-child(1) figure img")
    team2Picks = item.select(".row:nth-child(3) .col:nth-child(2) figure img")

    team1PicksFiltered = list(map(lambda pick: pick["alt"], team1Picks))
    team2PicksFiltered = list(map(lambda pick: pick["alt"], team2Picks))
    return (team1PicksFiltered, team2PicksFiltered)

def getBanData(game):
    
    team1Bans = item.select(".row:nth-child(5) .col:nth-child(1) figure img")
    team2Bans = item.select(".row:nth-child(5) .col:nth-child(3) figure img")

    team1BansFiltered = list(map(lambda ban: ban["alt"], team1Bans))
    team2BansFiltered = list(map(lambda ban: ban["alt"], team2Bans))
    return (team1BansFiltered, team2BansFiltered)

pp = pprint.PrettyPrinter(indent=1)
r = requests.get('https://heroeslounge.gg/match/view/4368')
html = r.text
parsedHTML = BeautifulSoup(html)
gamesData = parsedHTML.select("div.tab-content .tab-pane")
teamData = {}
for item in gamesData:
    teamNames = item.select(".media-body a")
    teamName1 = teamNames[0].text.strip()
    teamName2 = teamNames[1].text.strip()

    if teamName1 not in teamData:
        teamData[teamName1] = []
        teamData[teamName2] = []

    #Setup gameDataObjs
    team1Data = {
        "win": None,
        "picks": [],
        "bans": []
    }
    team2Data = {
        "win": None,
        "picks": [],
        "bans": []
    }

    pickData = getPickData(item)
    team1Data["picks"] = pickData[0]
    team2Data["picks"] = pickData[1]

    banData = getBanData(item)
    team1Data["bans"] = banData[0]
    team2Data["bans"] = banData[1]

    team1Data["win"] = len(item.select(".row .card.border .mb-2 .col-6:nth-child(1) .badge-success")) > 0
    team2Data["win"] = len(item.select(".row .card.border .mb-2 .col-6:nth-child(2) .badge-success")) > 0

    teamData[teamName1].append(team1Data)
    teamData[teamName2].append(team2Data)

#     print("Team1: ", teamName1)
#     print("Team2: ", teamName2)
pp.pprint(teamData)
# teamNames = gameData.select(".media-body a")
# print("Request: ", teamNames)
