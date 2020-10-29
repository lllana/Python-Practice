import pandas as pd

df_old = pd.read_csv('/datasets/music_log_old_en.csv')
df_new = pd.read_csv('/datasets/music_log_upd_en.csv')

median_old = df_old.groupby('user_id')['total_play_seconds'].sum().median()
# sum up 'total_play_seconds' for every user and find the median
median_new = df_new.groupby('user_id')['total_play_seconds'].sum().median()
# do the same for the new DataFrame

data = [
		'happiness', median_old,  median_new, median_new - median_old
	]
columns = ['metric', 'median_old', 'median_new', 'difference']

# create new DataFrame object
results = pd.DataFrame(data=[data],columns=columns) 

print(results)