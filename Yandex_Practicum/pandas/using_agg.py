import pandas as pd
logs = pd.read_csv('/datasets/logs.csv')
logs['email'] = logs['email'].fillna(value='')
logs.loc[logs['source'] == 'None', 'source'] = 'email'

logs_grouped = logs.groupby('source').agg({'purchase': ['count', 'sum']})

print(logs_grouped)