import json
import pandas
import statistics
from constants import *

def getCSVDataAsJson(url: str, columns: list):
    dataframe = pandas.read_csv(url, header=None)
    dataframe.columns = columns
    # uncomment to save to local file
    # dataframe.to_json('pick3morning.json', orient='records', indent=4)
    dataAsJsonStr = dataframe.to_json(orient='records', indent=4)
    result = json.loads(dataAsJsonStr)
    print(f'Total records found for {url}: {len(result)}')
    return result

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
    

def saveJsonToFile(data: any, fileName: str):
    pandas.DataFrame(data).to_json(fileName, orient='records', indent=4)
    