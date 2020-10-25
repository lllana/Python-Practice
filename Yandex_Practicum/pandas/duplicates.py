import pandas as pd

df = pd.read_csv('music_log_upd_nan.csv')

df = df.drop_duplicates().reset_index(drop=True)

print(df['genre_name'].unique())

df['genre_name'] = df['genre_name'].replace('электроника', 'electronic')