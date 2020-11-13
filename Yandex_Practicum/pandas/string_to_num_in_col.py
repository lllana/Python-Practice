import pandas as pd
data = pd.read_excel('/datasets/seo_data_eng.xlsx', sheet_name='traffic_data')
data = data[(data['subcategory_id'] != 'total')]

data['visits'] = data['visits'].astype('int')

data.info()