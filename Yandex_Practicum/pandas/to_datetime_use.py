import pandas as pd
position = pd.read_csv('/datasets/position.csv')

position['timestamp'] = pd.to_datetime(position['timestamp'], format = '%Y-%m-%dT%H:%M:%S')

print(position.head())

sorted_position = position.sort_values(by = 'level', ascending = False, inplace = False)