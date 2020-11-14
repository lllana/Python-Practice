import pandas as pd
data_final = pd.read_csv('/datasets/data_final_eng.csv')
data_pivot = data_final.pivot_table(index=['category_name', 'subcategory_name'], columns='source', values='visits', aggfunc='sum')
data_pivot['ratio'] = data_pivot['organic'] / data_pivot['direct']

print(data_pivot[data_pivot['direct'] > 1000].sort_values('ratio', ascending = False).tail(10))