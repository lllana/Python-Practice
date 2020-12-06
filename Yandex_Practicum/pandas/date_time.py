import pandas as pd

data = pd.read_csv('/datasets/visits_eng.csv', sep='\t')

data['date_time'] = pd.to_datetime(data['date_time'], format = '%Y-%m-%dT%H:%M:%S')

print(data.head())