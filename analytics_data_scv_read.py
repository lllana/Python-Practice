import pandas as pd 

#Read csv files and print needed colomns

csv_file = 'campaign_events.csv'
row_number = 38
col_list = ['Campaign', 'Event Action', 'New Users', 'Avg. Session Duration']
dwnd_btn = ['Free start click', 'Main \'Free Start\' Click', '\'Add Player\' click', 'Upper Download click', 'Lower Download click']

def read_file(csv_file):
    df = pd.read_csv(csv_file, skiprows = 6, usecols = col_list)
    result = df.head(row_number)
    
    
#campaign dictionary form
    campaign_dic = {}
    for i in result['Campaign']:
        if i in campaign_dic.keys() == True:
            pass
        else:
            campaign_dic[i] = 0
    
    #for i in result:
        #if i in campaign_dic and result['Event Action'] = 

    return campaign_dic

print(read_file(csv_file))

