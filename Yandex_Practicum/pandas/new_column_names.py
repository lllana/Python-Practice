import pandas as pd
support = pd.read_csv('/datasets/support_eng.csv')

support.set_axis(['user_id','type_message', 'type_id', 'timestamp'], axis = 'columns', inplace = True)

support.info()