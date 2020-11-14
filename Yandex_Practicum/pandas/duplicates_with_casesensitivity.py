import pandas as pd
stock = pd.read_csv('/datasets/stock_upd_eng.csv')
stock['item_lowercase'] = stock['item'].str.lower()

print(stock)