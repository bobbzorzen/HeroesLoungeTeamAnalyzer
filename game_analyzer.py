from game_data_gatherer import GameDataGatherer


class GameAnalyzer:

    def __add__(self, other):
        pass

    def __init__(self, gameUrl):
        print("Analyzing game: ", gameUrl)
        gameDataGatherer = GameDataGatherer(gameUrl)

        gameData = gameDataGatherer.gatherData()
        self.analysis = {}
        for team in gameData:
            self.analysis[team] = {
                "picks": self.getPickSummary(gameData[team]),
                "bans": self.getBanSummary(gameData[team])
            }
            print("TEAM: ", team)
            print("Analysis: ", self.analysis[team])

    def getPickSummary(self, games):
        summary = {}
        for game in games:
            for pick in game["picks"]:
                if pick not in summary:
                    summary[pick] = {"occurrances": 0, "wins": 0, "winrate": 0}
                if game["win"]:
                    summary[pick]["wins"] += 1
                summary[pick]["occurrances"] += 1
                summary[pick]["winrate"] = int((summary[pick]["wins"] / summary[pick]["occurrances"])*100)
        return summary

    def getBanSummary(self, games):
        summary = {}
        for game in games:
            for ban in game["bans"]:
                if ban not in summary:
                    summary[ban] = {"occurrances": 1}
                summary[ban]["occurrances"] += 1
        return summary
