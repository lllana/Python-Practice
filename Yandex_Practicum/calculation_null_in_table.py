import pandas as pd

df = pd.read_csv('music_log_upd_col.csv')

print(df.isnull().sum())