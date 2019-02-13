import requests
from bs4 import BeautifulSoup
from game_analyzer import GameAnalyzer

teamUrl = "https://heroeslounge.gg/team/view/RIDM"
r = requests.get(teamUrl)
html = r.text
parsedHTML = BeautifulSoup(html)
matches = parsedHTML.select("#activeSeasonMatches .tab-pane .card")
for matchRow in matches:
    isScheduledMatch = len(matchRow.select(".badge-warning")) > 0
    print("is scheduled match: ", isScheduledMatch)
    if not isScheduledMatch:
        matchLink = matchRow.select(".col-2 a")[0]
        gameAnalyzer = GameAnalyzer(matchLink["href"])
    # print("LINK: ", game)
