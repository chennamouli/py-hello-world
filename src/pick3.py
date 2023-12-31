import pandas
from collections import Counter
from datetime import date
from constants import *
from util import *

def getPick3Data():
    # data = getCSVDataAsJson([LOTTERY_BASE_URL + PICK3_MORNING_URL, LOTTERY_BASE_URL + PICK3_DAY_URL, LOTTERY_BASE_URL + PICK3_EVENING_URL, LOTTERY_BASE_URL + PICK3_NIGHT_URL], PICK3_COLUMNS)
    data = getCSVDataAsJson(['assets/pick3.csv'], PICK3_COLUMNS)
    saveCsvToFile(data, 'assets/pick3.csv') # Save csv data to 
    data = cleanUpData(data, PICK3_BUCKETS)
    data = sortByKey(data, 'Date')
    data = filterByDateRange(data, '2023-01-01', date.today().strftime('%Y-%m-%d')) # Read only specific data range
    saveJsonToFile(data, 'assets/pick3.json')
    return data

def analyseData():
    data = getPick3Data()
    # filterByKey(data, 'Number', 679)
    
    data = filterByDateRange(data, '2023-01-01', '2023-12-31') # To analyse specific data range
    all_numbers = getAllNumbers(data)
    most_repeated_numbers(all_numbers)
    print('@@@@@ total values: ', len(all_numbers.values))
    findHighProbabilityNumberList(all_numbers.values, 128)

    # print('all numbers: ', len(all_numbers))
    # calculateStatistics(all_numbers)
    # findRepeatedNumbers(all_numbers)
    # # drawHistogram(all_numbers, 20, 'Pick3 Numbers')
    
    # all_digits = getAllDigits(data)
    # calculateStatistics(all_digits)
    # findRepeatedNumbers(all_digits)
    # drawHistogram(all_digits, 10, 'Pick3 Digits')
    
    
    

analyseData()

# print(findBucketId([1, 4, 0], PICK3_BUCKETS))




