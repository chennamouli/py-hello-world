import pandas
from constants import *
from util import *

def getPick3Data():
    # data = getCSVDataAsJson(LOTTERY_BASE_URL + PICK3_MORNING_URL, PICK3_COLUMNS)
    data = getCSVDataAsJson('assets/pick3morning.csv', PICK3_COLUMNS)
    data = cleanUpData(data)
    saveJsonToFile(data, 'assets/pick3morning.json')
    
    all_numbers = pandas.DataFrame(data)['Number']
    calculateStatistics(all_numbers)
    return data

def cleanUpData(data: any):
    for index, item in enumerate(data):
    # for item in data:
        item['Date'] = str(item['Month']) +'-'+ str(item['Day']) +'-'+ str(item['Year'])
        item['Number'] = int(str(item['First_Digit']) + str(item['Second_Digit']) + str(item['Third_Digit']))
        item['Ball'] = item['Ball1'] or item['Ball2']
        del item['Ball1']
        del item['Ball2']
    return data




getPick3Data()


