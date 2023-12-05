import pandas
from collections import Counter
from constants import *
from util import *

def getPick3Data():
    data = getCSVDataAsJson([LOTTERY_BASE_URL + PICK3_MORNING_URL, LOTTERY_BASE_URL + PICK3_DAY_URL, LOTTERY_BASE_URL + PICK3_EVENING_URL, LOTTERY_BASE_URL + PICK3_NIGHT_URL], PICK3_COLUMNS)
    # data = getCSVDataAsJson(['assets/pick3.csv'], PICK3_COLUMNS)
    saveCsvToFile(data, 'assets/pick3.csv') # Save csv data to 
    data = cleanUpData(data)
    data = sortByKey(data, 'Date')
    saveJsonToFile(data, 'assets/pick3.json')
    return data

def analyseData():
    data = getPick3Data()
    data = filterByDateRange(data, '2023-10-03', '2023-10-05') # To analyse specific data range
    all_numbers = getAllNumbers(data)
    calculateStatistics(all_numbers)
    findRepeatedNumbers(all_numbers)
    # drawHistogram(all_numbers, 20, 'Pick3 Numbers')
    
    all_digits = getAllDigits(data)
    calculateStatistics(all_digits)
    findRepeatedNumbers(all_digits)
    # drawHistogram(all_digits, 10, 'Pick3 Digits')
    





analyseData()





