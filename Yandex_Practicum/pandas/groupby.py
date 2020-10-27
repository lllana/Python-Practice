import pandas as pd
df = pd.read_csv('/datasets/music_log_upd_en.csv')

user_playtime = df.groupby('user_id')['total_play_seconds'].sum()
user_plays = df.groupby('user_id').count()

print(user_playtime.head(5))
print(user_plays.head(5))
