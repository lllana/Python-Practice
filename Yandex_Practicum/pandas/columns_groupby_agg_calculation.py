import pandas as pd
logs = pd.read_csv('/datasets/logs.csv')
logs['email'] = logs['email'].fillna(value='')
logs.loc[logs['source'] == 'None', 'source'] = 'email'

logs_grouped = logs.groupby('source').agg({'purchase': ['count', 'sum']})

#column name is a tuple

logs_grouped['conversion'] = logs_grouped[('purchase', 'sum')] / logs_grouped[('purchase', 'count')]

print(logs_grouped)