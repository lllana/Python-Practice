import pandas as pd

measurements = [['Sun', 146, 152], 
                ['Moon', 0.36, 0.41], 
                ['Mercury', 82, 217], 
                ['Venus', 38, 261],
                ['Mars', 56, 401],
                ['Jupiter', 588, 968],
                ['Saturn', 1195, 1660],
                ['Uranus', 2750, 3150],
                ['Neptune', 4300, 4700],
                ['Halley\'s comet', 6, 5400]]
# Column names are stored in the header variable.
header = ['Celestial bodies ','MIN', 'MAX'] 

#transform list of lists to data frame
df = pd.DataFrame(data = measurements, columns = header)

new_titles = ['celestial_bodies', 'min_distance', 'max_distance'] 

#change the original data frame and nothing to return(None)
print(df.set_axis(['celestial_bodies', 'min_distance', 'max_distance'], axis= 'columns', inplace = True))

#NOT change the original data frame but return new one
print(df.set_axis(['celestial_bodies', 'min_distance', 'max_distance'], axis= 'columns', inplace = False))
