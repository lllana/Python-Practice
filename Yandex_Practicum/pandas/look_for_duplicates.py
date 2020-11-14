import pandas as pd
stock = pd.read_excel('/datasets/stock_eng.xlsx', sheet_name='storehouse')
print ('Duplicate entries in the table:', stock['item'].duplicated().sum())

print(stock['item'].value_counts())