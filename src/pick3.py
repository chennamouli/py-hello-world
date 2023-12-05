import pandas
from collections import Counter
from constants import *
from util import *

def getPick3Data():
    # data = getCSVDataAsJson(LOTTERY_BASE_URL + PICK3_MORNING_URL, PICK3_COLUMNS)
    data = getCSVDataAsJson('assets/pick3morning.csv', PICK3_COLUMNS)
    data = cleanUpData(data)
    saveJsonToFile(data, 'assets/pick3morning.json')
    
    all_numbers = getAllNumbers(data)
    calculateStatistics(all_numbers)
    findRepeatedNumbers(all_numbers)
    # drawHistogram(all_numbers, 20, 'Pick3 Numbers')
    
    all_digits = getAllDigits(data)
    calculateStatistics(all_digits)
    findRepeatedNumbers(all_digits)
    # drawHistogram(all_digits, 10, 'Pick3 Digits')
    
    filterByKey(data, 'Number', 115)
    filterByKey(data, 'Date', '10-24-2023')
    
    return data






getPick3Data()






