import pandas as pd
from datetime import date


def find_person(dict_users, strU):
    if dict_users.get(strU):
        return dict_users[strU]
    else:
        return 'Not Found'


quotes = {
    'close': [28.18, 27.71, 27.84, 27.32, 27.08],
    'date': [1465219800, 1465306200, 1465392600, 1465479000, 146556400],
    'high': [29.18, 30.71, 27.84, 27.32, 27.08],
    'low': [27.18, 25.71, 27.84, 27.32, 27.08],
    'open': [27.18, 25.71, 27.84, 27.32, 27.08],
    'volume': [94000, 45800, 65800, 50700, 68000]
}
attributes = ['close', 'date', 'high', 'low', 'open', 'volume']
quotesdf = pd.DataFrame(quotes, columns=attributes)

list1 = []
for i in range(len(quotesdf)):
    x = date.fromtimestamp(quotesdf['date'][i])
    y = date.strftime(x, '%Y/%m/%d')
    list1.append(y)
quotesdf_ori = pd.DataFrame(quotes, index=list1)
quotesdf = quotesdf_ori.drop(['date'], axis=1)

quotesdf['2016/06/07': '2016/06/08'][quotesdf.close > 40]
quotesdf.loc["date":'2017/06/03':'2017/06/07', ['open', 'close']]

list1 = []
tmpdf = quotesdf['2016/07/01':'2016/06/08']
for i in range(len(tmpdf)):
    list1.append(int(tmpdf.index[i][5:7]))
tmpdf['month'] = list1
print(tmpdf[tmpdf.close > tmpdf.open]['month'].value_counts())

if __name__ == "__main__":
    dict_users = {'Tom': 88888, 'Jerry': 5555555, 'Snoopy': 11111, 'Pooh': 12341234, 'Luffy': 1212121}
