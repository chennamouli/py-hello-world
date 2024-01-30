import pandas
from collections import Counter
from datetime import date
from constants import *
from util import *

def getLottoData():
    data = getCSVDataAsJson([LOTTERY_BASE_URL + LOTTO_URL], LOTTO_COLUMNS)
    # data = getCSVDataAsJson(['assets/lottotexas.csv'], LOTTO_COLUMNS)
    saveCsvToFile(data, 'assets/lottotexas.csv') # Save csv data to 
    data = cleanUpData(data, POWER_BALL_BUCKETS)
    data = sortByKey(data, 'Date')
    data = filterByDateRange(data, '2015-01-01', date.today().strftime('%Y-%m-%d')) # Read only specific data range
    saveJsonToFile(data, 'assets/lottotexas.json')
    # for item in data:
    #     findMatchingEvents(data, item['SortedNumberArray'], 3) 
    
    # value = '8-17-24-33-45-48'
    value = '3-15-24-31-48-51'
    value = '9-17-20-27-36-41'
    value = '6-11-28-30-41-52'
    findMatchingEvents(data, toNumArray(value), 3)
    findMatchingEvents(data, toNumArray(value), 4) # give this format
    printMissingNumbersInLast10Games(data[-11:])

    return data

def findMatchingEvents(data, inputNumArray, matchCount):
    matchItems = []
    for item in data:
        intersection_list = [value for value in item['SortedNumberArray'] if value in inputNumArray]
        if len(intersection_list) == matchCount:
            matchItems.append(item)
            print(f"Match found with match count {matchCount}: ", item['Date'], item['Number'], intersection_list, '***' if len(intersection_list) == 6 else '')
    if len(matchItems) > 0:
        print(len(matchItems))
        
def toNumArray(numbers_string):
    numbers_string = numbers_string.replace(" ", "").split('-')
    return [int(num) for num in numbers_string]

def printMissingNumbersInLast10Games(data):
    numbers = []
    for item in data:
        numbers = numbers + item['SortedNumberArray']
    most_repeated_numbers(numbers)
    numbers = list(set(numbers))
    print(f'Drawn Numbers found {len(numbers)}', numbers)
    missing_numbers = []
    for i in range(55):
        if i not in numbers:
            missing_numbers.append(i)
    print(f'Missing Numbers found {len(missing_numbers)}: ', missing_numbers)        

getLottoData()
print('\n')



# Most repeated numbers:  [29, 20, 34, 47, 37, 19, 39, 41, 49, 11, 22]
# Drawn Numbers found 37 [6, 7, 8, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 33, 34, 35, 37, 38, 39, 40, 41, 43, 46, 47, 49, 50, 51, 53]
# Missing Numbers found 23:  [0, 1, 2, 3, 4, 5, 9, 16, 25, 31, 32, 36, 42, 44, 45, 48, 52, 54, 55, 56, 57, 58, 59]

# Most repeated numbers:  [29, 47, 11, 34, 37, 13, 22, 51, 24, 43, 46]
# Drawn Numbers found 38 [6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 33, 34, 35, 37, 38, 39, 40, 41, 43, 46, 47, 49, 50, 51, 53]
# Missing Numbers found 17:  [0, 1, 2, 3, 4, 5, 15, 25, 31, 32, 36, 42, 44, 45, 48, 52, 54]


# 3 15 24 31 48 51 won $3
# 8 17 24 33 45 48
# 19 20 23 27 36 41


