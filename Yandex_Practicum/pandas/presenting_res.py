import pandas as pd

df_old = pd.read_csv('/datasets/music_log_old_en.csv')
df_new = pd.read_csv('/datasets/music_log_upd_en.csv')

# create an empty list called 'data'
data = []
genre = 'Pop'# specify the genre here

for df in (df_old, df_new):
    temp = []
    selection = df[(df['genre_name'] == genre) & (df['total_play_seconds'] > 0)]
    temp.append(selection['user_id'].count())
    temp.append(selection['total_play_seconds'].median())
    data.append(temp)
        
index = ['before', 'now']
# rows to be called 'before' and 'now'. Make a list with these titles. 
columns = ['count', 'median_playtime' ] 
# list with the titles 'count' and 'median_playtime' 
results = pd.DataFrame(data=data,columns=columns,index=index) 
# construct a new DataFrame. Remember to use data, index, and columns parameters. 

print(results)