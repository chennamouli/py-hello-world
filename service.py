import httplib2
import json
import csv
import pprint
import pandas
import numpy
from constants import LOTTERY_BASE_URL
from constants import PICK3_MORNING_URL


def getCSVDataAsJson(url: str, columns: list):
    dataframe = pandas.read_csv(url, header=None)
    dataframe.columns = columns;
    # dataframe.to_json('pick3morning.json', orient='records', indent=4)    # save to file
    dataAsJsonStr = dataframe.to_json(orient='records')
    result = json.loads(dataAsJsonStr)
    print(f'Total records found for {url}: {len(result)}')
    # print("getCSVDataAsJson: ", result)
    return result

def calculateStandardDeviation(data: list, field: str = 'Number'):
    all_numbers = pandas.DataFrame(data)[field]
    std_deviation_population = all_numbers.std()
    std_deviation_simple = numpy.std(all_numbers)
    print(f'Total Records={len(data)}, std_deviation_population={std_deviation_population}, std_deviation_simple={std_deviation_simple}')

def getPick3Data():
    columns = ['Event', 'Month', 'Day', 'Year', 'First_Digit', 'Second_Digit', 'Third_Digit', 'Ball1', 'Ball2']
    data = getCSVDataAsJson(LOTTERY_BASE_URL + PICK3_MORNING_URL, columns)
    for index, item in enumerate(data):
    # for item in data:
        item['Date'] = str(item['Month']) +'-'+ str(item['Day']) +'-'+ str(item['Year'])
        item['Number'] = int(str(item['First_Digit']) + str(item['Second_Digit']) + str(item['Third_Digit']))
        item['Ball'] = item['Ball1'] or item['Ball2']
        del item['Ball1']
        del item['Ball2']
    calculateStandardDeviation(data)
    return data



getPick3Data()


