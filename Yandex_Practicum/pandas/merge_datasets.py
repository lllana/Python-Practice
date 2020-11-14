import pandas as pd
data = pd.read_excel('/datasets/seo_data_eng.xlsx', sheet_name='traffic_data')
subcategory_dict = pd.read_excel('/datasets/seo_data_eng.xlsx', sheet_name='subcategory_ids')
category_dict = pd.read_excel('/datasets/seo_data_eng.xlsx', sheet_name='category_ids')
data_subcategory = data.merge(subcategory_dict, on='subcategory_id', how='left')

data_final = data_subcategory.merge(category_dict, on = 'category_id', how = 'left')

print(data_final.head(10))