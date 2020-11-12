import pandas as pd
transactions = pd.read_excel('/datasets/ids.xlsx')

transactions['amount'] = pd.to_numeric(transactions['amount'], errors = 'coerce')

print(transactions.tail(30))