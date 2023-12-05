import json
import pandas
import statistics
import numpy as np
from matplotlib import colors
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from collections import Counter
from constants import *

def getCSVDataAsJson(urls: list, columns: list):
    dataframesList = []
    for url in urls:
        print(f'Reading data from => {url}')
        dataframe = pandas.read_csv(url, header=None)
        dataframe.columns = columns
        dataframesList.append(dataframe)
    dataframes = pandas.concat(dataframesList, axis=0)
    result = dataframeToJson(dataframes)
    print(f'Total records found for {url}: {len(result)}')
    return result

def cleanUpData(data: any):
    for index, item in enumerate(data):
    # for item in data:
        item['Date'] = str(item['Year']) +'-'+ str(item['Month']).zfill(2) +'-'+ str(item['Day']).zfill(2) + drawEventTime(item)
        number = str(item['Num1']) + str(item['Num2']) + str(item['Num3'])
        if 'Num4' in item: number+= str(item['Num4'])
        if 'Num5' in item: number+= str(item['Num5'])

        item['Number'] = int(number)
        item['Ball'] = int(item['Ball1'] or item['Ball2'])
        del item['Ball1']
        del item['Ball2']
    return data

def sortByKey(data: list, key):
    print('Before sorting', data[0])
    sortedDataFrame = pandas.DataFrame(data).sort_values(by=key)
    sortedData = dataframeToJson(sortedDataFrame)
    print('After sorting', sortedData[0])
    return sortedData

def dataframeToJson(df):
    return json.loads(df.to_json(orient='records', indent=4))

def saveJsonToFile(data: any, fileName: str):
    pandas.DataFrame(data).to_json(fileName, orient='records', indent=4)
    
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
    all_numbers = pandas.DataFrame(data)['Number']
    # print([i for i in all_numbers]) # print all the numbers
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
    print(f'Total Repeated Numbers found: {len(repeated_numbers)} ==> ', repeated_numbers)
    return repeated_numbers

def filterByKey(data: list, key, value):
    matchFound = list(filter(lambda item: item[key] == value, data))
    print(f'Matching results based on {key} : ', json.dumps(matchFound, indent=4))
    return matchFound
    
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
    
