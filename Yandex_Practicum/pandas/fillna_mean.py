import pandas as pd
analytics_data=pd.read_csv('/datasets/web_analytics_data.csv')
age_avg = analytics_data['age'].mean()

analytics_data['age'].fillna(age_avg, inplace = True)

print(analytics_data.head(10))