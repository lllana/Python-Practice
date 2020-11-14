import pandas as pd
stock = pd.read_excel('/datasets/stock_eng.xlsx', sheet_name='storehouse')
xiaomi = stock[stock['item'] == 'Xiaomi Redmi 6A 16GB']['count'].sum()
huawei = stock[stock['item'] == 'HUAWEI P30 lite']['count'].sum()
stock['item'] = stock['item'].drop_duplicates()
stock = stock.dropna().reset_index(drop=True)

stock.loc[stock['item'] == 'Xiaomi Redmi 6A 16GB', 'count'] = xiaomi
#stock.loc[0, 'count'] = xiaomi
print(stock)