LOTTERY_BASE_URL = 'https://www.texaslottery.com/export/sites/lottery/Games/'

PICK3_MORNING_URL = 'Pick_3/Winning_Numbers/pick3morning.csv'
PICK3_DAY_URL = 'Pick_3/Winning_Numbers/pick3day.csv'
PICK3_EVENING_URL = 'Pick_3/Winning_Numbers/pick3evening.csv'
PICK3_NIGHT_URL = 'Pick_3/Winning_Numbers/pick3night.csv'

DAILY4_MORNING_URL = 'Daily_4/Winning_Numbers/daily4morning.csv'
DAILY4_DAY_URL = 'Daily_4/Winning_Numbers/daily4day.csv'
DAILY4_EVENING_URL = 'Daily_4/Winning_Numbers/daily4evening.csv'
DAILY4_NIGHT_URL = 'Daily_4/Winning_Numbers/daily4night.csv'

PICK3_COLUMNS = ['GameName', 'Month', 'Day', 'Year', 'Num1', 'Num2', 'Num3', 'Ball1', 'Ball2']
DAILY4_COLUMNS = ['GameName', 'Month', 'Day', 'Year', 'Num1', 'Num2', 'Num3', 'Num4', 'Ball1', 'Ball2']

PICK3_BUCKETS = [
    {'id': 1, "values": [5, 8, 3]},
    {'id': 2, 'values': [7, 2, 6]},
    {'id': 3, 'values': [4, 0, 1]},
    {'id': 4, 'values': [9, 5, 4]},
    {'id': 5, 'values': [2, 3, 7]},
    {'id': 6, "values": [6, 8, 7]},
    {'id': 7, 'values': [1, 4, 2]},
    {'id': 8, 'values': [8, 0, 7]},
    {'id': 9, 'values': [3, 6, 5]},
    {'id': 10, 'values': [5, 1, 8]}
]

MAX_PRINT_TO_CONSOLE_ITEMS = 25
FOUND_MANY = '...found many!**!**!**!**!**!**!**!**!**!'
