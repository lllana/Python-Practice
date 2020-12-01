import pandas as pd

df = pd.DataFrame({
    'From': ['Moscow', 'Moscow', 'St. Petersburg', 'St. Petersburg', 'St. Petersburg'], 
    'To': ['Rome', 'Rome', 'Rome', 'Barcelona', 'Barcelona'],
    'Is_Direct': [False, True, False, False, True],
        'Has_luggage': [True, False, False, True, False],
        'Price': [210, 192, 193, 201, 314],
        'Date_From': ['01.07.19', '01.07.19', '04.07.2019', '03.07.2019', '05.07.2019'],
        'Date_To': ['07.07.19', '07.07.19', '10.07.2019', '09.07.2019', '11.07.2019'],
        'Airline': ['Belavia', 'S7', 'Finnair', 'Swiss', 'Rossiya'],
        'Travel_time_from': [995, 230, 605, 365, 255],
        'Travel_time_to': [350, 225, 720, 355, 250],
})
print(df[1.5*df['Price'] < df['Price'].max()]) 

#Select rows where there's a layover and the return flight arrives by July 8 (i.e., not July 9, 10, or 11).
print(df[(df['Is_Direct'] == False) & ~ (df['From'].isin(['09.07.2020']))])