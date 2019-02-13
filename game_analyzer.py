from game_data_gatherer import GameDataGatherer


class GameAnalyzer:

    def __add__(self, other):
        if not isinstance(other, GameAnalyzer):
            raise Exception("Invalid operation '__add__' on type " + str(type(self)) + " and " + str(type(other)))

        for team in other.analysis:
            if team not in self.analysis:
                self.analysis[team] = {
                    "picks": other.analysis[team]["picks"],
                    "bans": other.analysis[team]["bans"]
                }
                continue
            for pick in other.analysis[team]["picks"]:
                if pick not in self.analysis[team]["picks"]:
                    self.analysis[team]["picks"][pick] = {"occurrances": 0, "wins": 0, "winrate": 0}
                self.analysis[team]["picks"][pick]["wins"] += other.analysis[team]["picks"][pick]["wins"]
                self.analysis[team]["picks"][pick]["occurrances"] += 1
                self.analysis[team]["picks"][pick]["winrate"] = int((self.analysis[team]["picks"][pick]["wins"] / self.analysis[team]["picks"][pick]["occurrances"])*100)
            for ban in other.analysis[team]["bans"]:
                if ban not in self.analysis[team]["bans"]:
                    self.analysis[team]["bans"][ban] = {"occurrances": 1}
                self.analysis[team]["bans"][ban]["occurrances"] += 1
        return self

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
            # print("TEAM: ", team)
            # print("Analysis: ", self.analysis[team])

    def getPickSummary(self, games):
        summary = {}
        for game in games:
            for pick in game["picks"]:
                if(pick == ""):
                    continue
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
                if(ban == ""):
                    continue
                if ban not in summary:
                    summary[ban] = {"occurrances": 1}
                summary[ban]["occurrances"] += 1
        return summary
