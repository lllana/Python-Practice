import pandas as pd

df = pd.read_csv('music_log_upd_nan.csv')

#delete duplicates
df = df.drop_duplicates().reset_index(drop=True)

#looking for unique names in the df
print(df['genre_name'].unique())

#replace values in a column
df['genre_name'] = df['genre_name'].replace('электроника', 'electronic')

#count instances of value in a table with condition inside
count_variable = df[df['genre_name'] == 'selected_value']['genre_name'].count() 
print(count_variable)