from game_data_gatherer import GameDataGatherer


class GameAnalyzer:

    def __init__(self):
        gameDataGatherer = GameDataGatherer("https://heroeslounge.gg/match/view/4368")

        gameData = gameDataGatherer.gatherData()

        for team in gameData:
            print("TEAM: ", team)
        # print("Gamedata: ", gameData)
