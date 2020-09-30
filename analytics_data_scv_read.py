import pandas as pd 

col_list = ['Campaign', 'Event Action', 'New Users']
df = pd.read_csv('campaign_events.csv', skiprows = 6, usecols = col_list)
print(df.head(24))

