import pandas as pd

df = pd.read_csv('music_log_upd_col.csv')

print(df.isnull().sum())

df['track_name'].fillna('unknown', inplace = True)

df['genre_name'] = df['artist_name'].dropna()
