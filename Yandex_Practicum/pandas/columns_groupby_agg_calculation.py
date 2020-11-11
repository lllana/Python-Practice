import pandas as pd
logs = pd.read_csv('/datasets/logs.csv')
logs['email'] = logs['email'].fillna(value='')
logs.loc[logs['source'] == 'None', 'source'] = 'email'

logs_grouped = logs.groupby('source').agg({'purchase': ['count', 'sum']})

#column name is a tuple

logs_grouped['conversion'] = logs_grouped[('purchase', 'sum')] / logs_grouped[('purchase', 'count')]

#find out columns names
print(logs_grouped.columns.tolist())

print(logs_grouped)

#df.columns = df.columns.droplevel(0)