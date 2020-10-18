import pandas as pd

music = [
        ['Queen', 'Love of my life'],
        ['Queen', 'Under pressure'],
        ['Palina', 'Pinki'],
        ['Palina', 'Belarussian song'],
        ['Goldplay', 'Up&Up']
]
entries = ['artist', 'track']

playlist = pd.DataFrame(data = music, columns = entries)

print(playlist)