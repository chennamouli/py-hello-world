import pandas
from collections import Counter
from constants import *
from util import *

def getPick4Data():
    # data = getCSVDataAsJson(LOTTERY_BASE_URL + DAILY4_MORNING_URL, DAILY4_COLUMNS)
    data = getCSVDataAsJson('assets/daily4morning.csv', DAILY4_COLUMNS)
    data = cleanUpData(data)
    saveJsonToFile(data, 'assets/daily4morning.json')
    
    all_numbers = getAllNumbers(data)
    calculateStatistics(all_numbers)
    findRepeatedNumbers(all_numbers)
    # drawHistogram(all_numbers, 20, 'Pick3 Numbers')
    
    all_digits = getAllDigits(data)
    calculateStatistics(all_digits)
    findRepeatedNumbers(all_digits)
    # drawHistogram(all_digits, 10, 'Pick3 Digits')
    return data






getPick4Data()





