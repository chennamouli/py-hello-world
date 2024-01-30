import pandas
from collections import Counter
from datetime import date
import numpy as np
from constants import *
from util import *

def getData():
    data = getCSVDataAsJson([LOTTERY_BASE_URL + CASH_FIVE_URL], CASH_FIVE_COLUMNS)
    # data = getCSVDataAsJson(['assets/cashfive.csv'], CASH_FIVE_COLUMNS)
    saveCsvToFile(data, 'assets/cashfive.csv') # Save csv data to 
    data = cleanUpData2(data, CASH_FIVE_BUCKETS)
    # data = sortByKey(data, 'Date')
    # Sort the list of objects by the "Date" field
    data = sorted(data, key=lambda x: datetime.fromisoformat(x["Date"]), reverse=True)
    data = filterByDateRange(data, '2023-01-01', date.today().strftime('%Y-%m-%d')) # Read only specific data range
    checkForRepeatedNumbers(data, 1)
    checkForRepeatedNumbers(data, 2)
    checkForRepeatedNumbers(data, 3)
    checkForRepeatedNumbers(data, 4)
    checkForRepeatedNumbers(data, 5)
    checkForRepeatedNumbers(data, 6)
    checkForRepeatedNumbers(data, 7)
    listDrawnNumbers(data, 6)
    saveJsonToFile(data, 'assets/cashfive.json')
    return data

def cleanUpData2(data: any, bucket_list: list):
    for index, item in enumerate(data):
    # for item in data:
        item['Date'] = str(item['Year']) +'-'+ str(item['Month']).zfill(2) +'-'+ str(item['Day']).zfill(2) + drawEventTime(item)
        number = str(item['Num1']) + str(item['Num2']) + str(item['Num3'])
        if 'Num4' in item: number+= str(item['Num4'])
        if 'Num5' in item: number+= str(item['Num5'])
        if 'Num5' in item:
            numberArray = [str(item['Num1']), str(item['Num2']), str(item['Num3']), str(item['Num4']), str(item['Num5'])]
            # Convert string array to int array
            numberArray = [int(num) for num in numberArray]
            numberArray.sort()
            item['SortedNumberArray'] = numberArray
            numberAsIs = [str(num) for num in numberArray]
            numberAsIs = "-".join(numberAsIs)
            number = numberAsIs
        
        item['Date'] = item['Date']
        item['Number'] = number
        item['Num1'] = item['SortedNumberArray'][0]
        item['Num2'] = item['SortedNumberArray'][1]
        item['Num3'] = item['SortedNumberArray'][2]
        item['Num4'] = item['SortedNumberArray'][3]
        item['Num5'] = item['SortedNumberArray'][4]
        item['SortedNumberArray'] = item['SortedNumberArray']
        item['OddNumbersCount'] = countOddNumbers(item['SortedNumberArray'])
    
        del item['Year']
        del item['Month']
        del item['Day']
    return data

def countOddNumbers(list): 
    count_odd = 0
    for x in list:
        if x % 2:
            count_odd += 1
    return count_odd

def checkForRepeatedNumbers(data: any, lastNgames: int):
    for index, item in enumerate(data):
        current_sorted_array = item["SortedNumberArray"]
        previous_sorted_arrays = [item["SortedNumberArray"] for item in data[(index+1):(index+1+lastNgames)]]
        previous_sorted_merged_arrays = np.concatenate(previous_sorted_arrays) if len(previous_sorted_arrays) != 0 else [[]]
        common_values = np.intersect1d(current_sorted_array, previous_sorted_merged_arrays)
        item['RepeatedNumbersFromLast'+str(lastNgames)+'Games'] = "-".join([str(num) for num in common_values])
        item['RepeatedNumbersFromLast'+str(lastNgames)+'GamesCount'] = len(common_values)
        if len(common_values) > 3:
            # print(f'Date {item["Date"]} -> Current {current_sorted_array} Prvious {previous_sorted_merged_arrays}, Common {common_values}')
            print(' ')
 
def listDrawnNumbers(data: any, lastNgames: int):
    for index, item in enumerate(data):
        all_arrays = [item["SortedNumberArray"] for item in data[(index):(index+lastNgames)]]
        print('all_arrays', all_arrays)
        all_arrays_merged = set(np.concatenate(all_arrays) if len(all_arrays) != 0 else [[]])
        all_numbers = set(range(1, 36))
        missing_numbers = all_numbers - all_arrays_merged
        print('Drawn: ', all_arrays_merged)
        print('Missing: ', sorted(missing_numbers))

getData()