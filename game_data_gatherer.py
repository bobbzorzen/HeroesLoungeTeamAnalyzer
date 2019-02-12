import requests
import pprint
from bs4 import BeautifulSoup


class GameDataGatherer:
    def __init__(self, gameUrl):
        self.gameUrl = gameUrl

    def getPickData(self, game):
        team1Picks = game.select(".row")[2].select(".col")[0].select("figure img")
        team2Picks = game.select(".row")[2].select(".col")[1].select("figure img")

        team1PicksFiltered = list(map(lambda pick: pick["alt"], team1Picks))
        team2PicksFiltered = list(map(lambda pick: pick["alt"], team2Picks))
        return (team1PicksFiltered, team2PicksFiltered)

    def getBanData(self, game):
        team1Bans = game.select(".row")[4].select(".col")[0].select("figure img")
        team2Bans = game.select(".row")[4].select(".col")[2].select("figure img")

        team1BansFiltered = list(map(lambda ban: ban["alt"], team1Bans))
        team2BansFiltered = list(map(lambda ban: ban["alt"], team2Bans))
        return (team1BansFiltered, team2BansFiltered)

    def gatherData(self):
        pp = pprint.PrettyPrinter(indent=1)
        r = requests.get(self.gameUrl)
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

            # Setup gameDataObjs
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

            pickData = self.getPickData(item)
            team1Data["picks"] = pickData[0]
            team2Data["picks"] = pickData[1]

            banData = self.getBanData(item)
            team1Data["bans"] = banData[0]
            team2Data["bans"] = banData[1]

            team1Data["win"] = len(item.select(".row .card.border .mb-2 .col-6")[0].select(".badge-success")) > 0
            team2Data["win"] = len(item.select(".row .card.border .mb-2 .col-6")[1].select(".badge-success")) > 0

            teamData[teamName1].append(team1Data)
            teamData[teamName2].append(team2Data)

        # pp.pprint(teamData)
        return teamData

