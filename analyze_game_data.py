from game_data_gatherer import GameDataGatherer

gameDataGatherer = GameDataGatherer("https://heroeslounge.gg/match/view/4368")

gameData = gameDataGatherer.gatherData()
print("Gamedata: ", gameData)