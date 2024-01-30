import pandas
from collections import Counter
from datetime import date
from constants import *
from util import *

def getPowerBallData():
    # data = getCSVDataAsJson([LOTTERY_BASE_URL + POWER_BALL_URL], POWER_BALL_COLUMNS)
    data = getCSVDataAsJson(['assets/powerball.csv'], POWER_BALL_COLUMNS)
    saveCsvToFile(data, 'assets/powerball.csv') # Save csv data to 
    data = cleanUpData(data, POWER_BALL_BUCKETS)
    data = sortByKey(data, 'Date')
    data = filterByDateRange(data, '2015-01-01', date.today().strftime('%Y-%m-%d')) # Read only specific data range
    saveJsonToFile(data, 'assets/powerball.json')
    # for item in data:
    #     findMatchingEventsAtleast3(data, item['SortedNumberArray']) 
    findMatchingEventsAtleast3(data, toNumArray('27 - 35 - 41 - 56 - 60')) # give this format
    return data

def findMatchingEventsAtleast3(data, inputNumArray):
    matchItems = []
    for item in data:
        intersection_list = [value for value in item['SortedNumberArray'] if value in inputNumArray]
        if len(intersection_list) == 3:
            matchItems.append(item)
            print("Match found with 3 numbers: ", item['Date'], item['Number'], intersection_list, '***' if len(intersection_list) == 4 else '')
    if len(matchItems) > 0:
        print(len(matchItems))
    # matchItems = list(set(matchItems))
    # for item in matchItems:
    #     print("findMatchingEventsAtleast3: ", item['Date'], item['Number'])


def toNumArray(numbers_string):
    numbers_string = numbers_string.replace(" ", "").split('-')
    return [int(num) for num in numbers_string]


getPowerBallData()
print('\n')