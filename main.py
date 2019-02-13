import csv
import json
import requests
from bs4 import BeautifulSoup
from game_analyzer import GameAnalyzer

teamUrl = "https://heroeslounge.gg/team/view/B2C"
teamName = "Body Block Crew"
r = requests.get(teamUrl)
html = r.text
parsedHTML = BeautifulSoup(html)
matches = parsedHTML.select("#activeSeasonMatches .tab-pane .card")
finalAnalysis = None
for matchRow in matches:
    isScheduledMatch = len(matchRow.select(".badge-warning")) > 0
    print("is scheduled match: ", isScheduledMatch)
    if not isScheduledMatch:
        matchLink = matchRow.select(".col-2 a")[0]
        gameAnalyzer = GameAnalyzer(matchLink["href"])
        if(finalAnalysis is not None):
            finalAnalysis = finalAnalysis + gameAnalyzer
        else:
            finalAnalysis = gameAnalyzer
teamData = finalAnalysis.analysis[teamName]

with open('output/' + teamName + '_teamData.json', 'w') as outfile:
    json.dump(teamData, outfile)
