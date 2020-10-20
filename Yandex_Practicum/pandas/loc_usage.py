import pandas as pd

df = pd.read_csv('music_log.csv')

pop = df.loc[df['genre'] == 'pop']
pop_time = pop.loc[:,'total play']
pop_haters = pop_time.loc[pop_time <= 5].count()


rock = df.loc[df['genre'] == 'rock']
rock_time = rock.loc[:,'total play']
rock_haters = rock_time.loc[rock_time <= 5].count()

pop_skip = pop_haters / pop.shape[0]
rock_skip = rock_haters / rock.shape[0]

print('Percentage of rock tracks skipped: {:.1%}'.format(rock_skip))
print('Percentage of pop tracks skipped: {:.1%}'.format(pop_skip))