import pandas as pd
analytics_data = pd.read_csv('/datasets/web_analytics_data.csv')

desktop_data = analytics_data[analytics_data["device_type"] == 'desktop']

print(desktop_data.head())