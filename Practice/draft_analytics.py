
dwnd_buttons = 
campaign_dic = {}
def dic_build(result):
    for i in result['Campaign']:
        print(i)
        if i in campaign_dic.keys() == True:
            pass
        else:
            campaign_dic[i] = 0
            print(campaign_dic)
    print(campaign_dic)


    #Execute the functions written
def main():
    while True:
        read_file(csv_file)