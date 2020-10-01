import pandas as pd 

#Read csv files and print needed colomns

csv_file = 'campaign_events.csv'
row_number = 38
col_list = ['Campaign', 'Event Action', 'New Users', 'Avg. Session Duration']
dwnd_btn = ['Free start click', 'Main \'Free Start\' Click', 'Add Player\' click', 'Upper Download click', 'Lower Download click']

def read_file(csv_file):
    df = pd.read_csv(csv_file, skiprows = 6, usecols = col_list)
    result = df.head(row_number)
    
    #campaign dictionary form
    campaign_dic = {}
    for _, row in result.iterrows():
        campaign_name = row['Campaign']
        action_name = row['Event Action']
        new_users = row['New Users']    

        if action_name in dwnd_btn:
            if campaign_name in campaign_dic:
                campaign_dic[campaign_name] += new_users 
            else:
                campaign_dic[campaign_name] = new_users

    return campaign_dic

print(read_file(csv_file))

