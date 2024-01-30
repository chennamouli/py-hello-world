import pandas
from collections import Counter
from datetime import date
from constants import *
from util import *


def getPick4Data():
    data = getCSVDataAsJson([LOTTERY_BASE_URL + DAILY4_MORNING_URL, LOTTERY_BASE_URL + DAILY4_DAY_URL, LOTTERY_BASE_URL + DAILY4_EVENING_URL, LOTTERY_BASE_URL + DAILY4_NIGHT_URL], DAILY4_COLUMNS)
    # data = getCSVDataAsJson(['assets/daily4.csv'], PICK3_COLUMNS)
    saveCsvToFile(data, 'assets/daily4.csv') # Save csv data to 
    data = cleanUpData(data, [])
    data = filterByDateRange(data, '2020-01-01', date.today().strftime('%Y-%m-%d')) # Read only specific data range
    data = sortByKey(data, 'Date')
    saveJsonToFile(data, 'assets/daily4.json')
    return data

def analyseData():
    data = getPick4Data()
    # filterByKey(data, 'Number', 556)
    
    # data = filterByDateRange(data, '2023-12-05', '2023-12-05') # To analyse specific data range
    all_numbers = getAllNumbers(data)
    # calculateStatistics(all_numbers)
    findRepeatedNumbers(all_numbers)
    # drawHistogram(all_numbers, 20, 'Pick3 Numbers')
    
    all_digits = getAllDigits(data)
    # calculateStatistics(all_digits)
    findRepeatedNumbers(all_digits)
    # drawHistogram(all_digits, 10, 'Pick3 Digits')
    
    
    

analyseData()