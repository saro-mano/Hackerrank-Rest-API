import math
import os
import random
import re
import sys


#
# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year
#
import requests

def params(team, year, page, whichTeam, compeition):
    print ({
        'year': str(year),
        'team'+str(whichTeam): team,
        'page': page
    })
    return {
        'year': str(year),
        'team'+str(whichTeam): team,
        'page': page,
        'competition': compeition
    }
    
def handleRequest(team, year, page, whichTeam=1, compeition=''):
    URL = 'https://jsonmock.hackerrank.com/api/football_matches'
    r = requests.get(url = URL, params = params(team, year, page, whichTeam, compeition))
    data = r.json()
    return data
    
def handleData(team, whichTeam,compeition):
    teamNum = 'team' + str(whichTeam) + 'goals'
    print(teamNum)
    goals = 0
    r = handleRequest(team, year, 1, whichTeam, competition)
    totalPages = r['total_pages']
    perPage = r['per_page']
    # request data for team 1
    for i in range(1, totalPages+1):
        # append data to the dict
        r = handleRequest(team, year, i, whichTeam, compeition)
        print('r for page {0} data is {1}'.format(i, r))
        try:
            for j in range(0, perPage):
                goals += int(r['data'][j][teamNum])
        except:
            pass
        print(goals)
    return goals
    
def getTotalGoals(team, year, compeition):
    totalGoals = 0
    # first request to get the pagination details
    totalGoals += handleData(team, 1, compeition)
    totalGoals += handleData(team, 2, compeition)
    return totalGoals

def getWinnerTotalGoals(competition, year):
    # Write your code here
    URL = 'https://jsonmock.hackerrank.com/api/football_competitions'
    params = {
        'name': competition,
        'year': str(year)
    }
    r = requests.get(URL, params).json()
    print(r)
    team = r['data'][0]['winner']
    return getTotalGoals(team, year, competition)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    competition = input()

    year = int(input().strip())

    result = getWinnerTotalGoals(competition, year)

    fptr.write(str(result) + '\n')

    fptr.close()
