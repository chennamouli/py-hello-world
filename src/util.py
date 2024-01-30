import json
import pandas
import statistics
import numpy as np
from datetime import datetime
from matplotlib import colors
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from collections import Counter
from constants import *

def getCSVDataAsJson(urls: list, columns: list):
    dataframesList = []
    for url in urls:
        print(f'Reading data from => {url}')
        dataframe = pandas.read_csv(url, header=None, on_bad_lines='skip')
        dataframe.columns = columns
        dataframesList.append(dataframe)
    dataframes = pandas.concat(dataframesList, axis=0)
    result = dataframeToJson(dataframes)
    print(f'Total records found for {url}: {len(result)}')
    return result

def cleanUpData(data: any, bucket_list: list):
    for index, item in enumerate(data):
    # for item in data:
        item['Date'] = str(item['Year']) +'-'+ str(item['Month']).zfill(2) +'-'+ str(item['Day']).zfill(2) + drawEventTime(item)
        number = str(item['Num1']) + str(item['Num2']) + str(item['Num3'])
        if 'Num4' in item: number+= str(item['Num4'])
        if 'Num5' in item: number+= str(item['Num5'])
        if 'Num6' in item: number+= str(item['Num6'])
        # item['Ball'] = int(item['Ball1'] or item['Ball2'] if 'Ball2' in item else 999)
        # item['Ball'] = int(item['Ball1'] if 'Ball1' in item else item['Ball2'] if 'Ball2' in item else 999)
        ball1 = item.get('Ball1', None)
        ball2 = item.get('Ball2', None)
        result = int(ball1) if ball1 is not None else int(ball2) if ball2 is not None else 999


        # if 'Num5' in item:
        numberArray = [str(item['Num1']), str(item['Num2']), str(item['Num3'])]
        if 'Num4' in item: numberArray.append(str(item['Num4']));
        if 'Num5' in item: numberArray.append(str(item['Num5']));
        if 'Num6' in item: numberArray.append(str(item['Num6']));
        # Convert string array to int array
        
        numberAsIs = [str(num) for num in numberArray]
        
        numberAsIs = "-".join(numberAsIs)
        number = numberAsIs
        numberArray = [int(num) for num in numberArray]
        numberArray.sort()
        item['SortedDigitsNumber'] = ''.join(map(str, (sorted(numberArray))))
        item['SortedNumberArray'] = numberArray
        
        
        item['Number'] = number
        
        item['SumOfDigits'] = item['Num1'] + item['Num2'] + item['Num3']
        item['Bucket'] = findBucketId([item['Num1'], item['Num2'], item['Num3']], bucket_list)
        item['RepeatedNumbers'] = hasRepeatedNumbers([item['Num1'], item['Num2'], item['Num3']])
        item['Quarter'] = findNumberQuarterRange([item['Num1'], item['Num2'], item['Num3']])
        if 'Ball1' in item: del item['Ball1']
        if 'Ball2' in item: del item['Ball2']
        del item['Year']
        del item['Month']
        del item['Day']
    return data

def sortByKey(data: list, key):
    # print('Before sorting', data[0])
    sortedDataFrame = pandas.DataFrame(data).sort_values(by=key)
    sortedData = dataframeToJson(sortedDataFrame)
    # print('After sorting', sortedData[0])
    return sortedData

def dataframeToJson(df):
    return json.loads(df.to_json(orient='records', indent=4))

def saveJsonToFile(data: any, fileName: str):
    pandas.DataFrame(data).to_json(fileName, orient='records', indent=4)
    
def saveCsvToFile(data: any, fileName: str):
    pandas.DataFrame(data).to_csv(fileName, header=0, index=0)
    
def drawEventTime(event):
    if str(event['GameName']).endswith('Morning'):
        return 'T09:50:00'
    if str(event['GameName']).endswith('Day'):
        return 'T12:17:00'
    if str(event['GameName']).endswith('Evening'):
        return 'T17:50:00'
    else:
        return 'T22:02:00'

def getAllNumbers(data: any): 
    all_numbers = pandas.DataFrame(data)['SortedDigitsNumber']
    # print([i for i in all_numbers] if len(all_numbers) < MAX_PRINT_TO_CONSOLE_ITEMS else FOUND_MANY) # print all the numbers
    return all_numbers

def getAllDigits(data: any): 
    list = []
    for item in data:
        list.append(item['Num1'])
        list.append(item['Num2'])
        list.append(item['Num3'])
        if 'Num4' in item: list.append(item['Num4'])
        if 'Num5' in item: list.append(item['Num5'])
    # print(f'All Digits: ', list)
    return list

def calculateStatistics(data: list):
    stats = {}
    stats['mean'] = statistics.mean(data)   # avg
    stats['median'] = statistics.median(data) # mid point
    stats['mode'] = statistics.mode(data)   # most common value
    # Standard deviation is a number that describes how spread out the values are.
    # A low standard deviation means that most of the numbers are close to the mean (average) value.
    # A high standard deviation means that the values are spread out over a wider range.
    stats['stdev'] = statistics.stdev(data)
    print(f'Statistics: ', json.dumps(stats, indent=4))
    return stats
    
def findRepeatedNumbers(data: list):
    repeated_numbers = [k for k,v in Counter(data).items() if v>1]
    # print(f'Total Repeated Numbers found: {len(repeated_numbers)} ==> ', repeated_numbers if len(repeated_numbers) < MAX_PRINT_TO_CONSOLE_ITEMS else FOUND_MANY)
    return repeated_numbers

def filterByKey(data: list, key, value):
    matchFound = list(filter(lambda item: item[key] == value or str(item[key]).startswith(str(value)), data))
    print(f'Matching results based on {key}({value}), found {len(matchFound)} : ', json.dumps(matchFound, indent=4) if len(matchFound) < MAX_PRINT_TO_CONSOLE_ITEMS else FOUND_MANY)
    return matchFound

def filterByDateRange(data: list, startDate: str, endDate: str):
    startDt = datetime.fromisoformat(startDate)
    endDt = datetime.fromisoformat(endDate+'T23:59:59')
    matchFound = list(filter(lambda item: startDt <= datetime.fromisoformat(str(item['Date'])) and datetime.fromisoformat(str(item['Date'])) <= endDt, data))
    for item in data:
        dt = datetime.fromisoformat(str(item['Date']))
    # print(f'Matching results based on the date range from {startDt} to {endDt}, found {len(matchFound)} : ', json.dumps(matchFound, indent=4) if len(matchFound) < MAX_PRINT_TO_CONSOLE_ITEMS else FOUND_MANY)
    return matchFound

def findBucketId(input_list, bucket_list):
    if len(bucket_list) == 0:
        return 0
    result = [bucket["id"] for bucket in bucket_list if all(elem in bucket["values"] for elem in input_list)]
    return result[0] if result else 0
    
def hasRepeatedNumbers(values: list):
    return len(values) != len(set(values))

def findNumberQuarterRange(values: list):
    isPick3 = len(values) == 3
    total_values = 1000 if isPick3 else 10000
    number = int(''.join(map(str, values)))
    return 1 if number <= total_values/4 else 2 if number <= total_values/2 else 3 if number <= total_values*(3/4) else 4
    
def most_repeated_numbers(arr):
    # Use Counter to count occurrences of each element
    counts = Counter(arr)
    # print('most_repeated_numbers counter: ', counts.most_common(2))
    numbers = get_first_n_keys(counts, 11) 
    print('Most repeated numbers: ', numbers)
    return numbers   
   
def get_first_n_keys(counter, n):
    return [key for key, _ in counter.most_common(n)]
   
def is_array_contained(arr1, arr2):
    return all(elem in arr1 for elem in arr2)

def can_be_formed(number, allowed_digits):
    return set(map(int, str(number))) <= set(allowed_digits)

def find_numbers_with_digits(data, allowed_digits):
    result = []
    for number in data:
        if can_be_formed(number, allowed_digits):
            result.append(number)
    return result

def findHighProbabilityNumberList(numbers, value):
    result = {}
    for i in range(10):
        for j in range(10):
            valueArray = list({int(digit) for digit in str(value) + str(i) + str(j)}) #list(set(map(int, str(value) + str(i))))
            # if len(valueArray) == len(list(set(map(int, str(value))))):
            if len(valueArray) != 5:
                continue
            foundMatches = find_numbers_with_digits(numbers, valueArray)
            if len(foundMatches) > 0:
                key = ''.join(map(str, sorted(valueArray)))
                result[key] = result.get(key, 0) + len(foundMatches)
    print("findHighProbabilityNumberList: ", result)
    return result


def drawHistogram(x: list, bins: int, title: str):
    n_bins = bins
    legend = ['Distribution']
    
    # Creating histogram
    fig, axs = plt.subplots(1, 1,
                            figsize =(10, 7), 
                            tight_layout = True)
    
    # Remove axes splines 
    for s in ['top', 'bottom', 'left', 'right']: 
        axs.spines[s].set_visible(False) 
    
    # Remove x, y ticks
    axs.xaxis.set_ticks_position('none') 
    axs.yaxis.set_ticks_position('none') 
    
    # Add padding between axes and labels 
    axs.xaxis.set_tick_params(pad = 5) 
    axs.yaxis.set_tick_params(pad = 10) 
    
    # Add x, y gridlines 
    axs.grid(color ='grey', 
            linestyle ='-.', linewidth = 1, 
            alpha = 0.6) 
    
    # Add Text watermark 
    # fig.text(0.9, 0.15, title, 
    #         fontsize = 12, 
    #         color ='red',
    #         ha ='right',
    #         va ='bottom', 
    #         alpha = 0.7) 
    
    # Creating histogram
    N, bins, patches = axs.hist(x, bins = n_bins)
    
    # Setting color
    fracs = ((N**(1 / 5)) / N.max())
    norm = colors.Normalize(fracs.min(), fracs.max())
    
    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)
    
    # Adding extra features    
    plt.xlabel("X-axis")
    plt.ylabel("y-axis")
    plt.legend(legend)
    plt.title(title + ' histogram')
    
    # Show plot
    plt.show()
    
