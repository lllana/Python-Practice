# columns are [0]title [1]year [2]rating [3]length(min) [4]genre [5]budget($mil) [6]box_office_gross($mil)
oscar_data = [
    ["The Shape of Water", 2017, 6.914, 123, ['sci-fi', 'drama'], 19.4, 195.243464],
    ["Moonlight", 2016, 6.151, 110, ['drama'], 1.5, 65.046687],
    ["Spotlight", 2015, 7.489, 129, ['drama', 'crime', 'history'], 20.0, 88.346473],
    ["Birdman", 2014, 7.604, 119, ['drama', 'comedy'], 18.0, 103.215094],
    ["12 Years a Slave", 2013, 7.71, 133, ['drama', 'biography', 'history'], 20.0, 178.371993],
    ["Argo", 2012, 7.517, 120, ['thriller', 'drama', 'biography'], 44.5, 232.324128],
    ["The Artist", 2011, 7.942, 96, ['drama', 'melodrama', 'comedy'], 15.0, 133.432856],
    ["The King\'s Speech", 2010, 7.977, 118, ['drama', 'biography', 'history'], 15.0, 414.211549],
    ["The Hurt Locker", 2008, 7.298, 126, ['thriller', 'drama', 'war', 'history'], 15.0, 49.230772],
    ["Slumdog Millionaire", 2008, 7.724, 120, ['drama', 'melodrama'], 15.0, 377.910544],
    ["No Country for Old Men", 2007, 7.726, 122, ['thriller', 'drama', 'crime'], 25.0, 171.627166],
    ["The Departed", 2006, 8.456, 151, ['thriller', 'drama', 'crime'], 90.0, 289.847354],
    ["Crash", 2004, 7.896, 108, ['thriller', 'drama', 'crime'], 6.5, 98.410061],
    ["Million Dollar Baby", 2004, 8.075, 132, ['drama', 'sport'], 30.0, 216.763646],
    ["The Lord of the Rings: Return of the King", 2003, 8.617, 201, ['fantasy', 'drama', 'adventure'], 94.0, 1119.110941],
    ["Chicago", 2002, 7.669, 113, ['musical', 'comedy', 'crime'], 45.0, 306.776732],
    ['A Beautiful Mind', 2001, 8.557, 135, ['drama', 'biography', 'melodrama'], 58.0, 313.542341],
    ["Gladiator", 2000, 8.585, 155, ['action', 'drama', 'adventure'], 103.0, 457.640427],
    ["American Beauty", 1999, 7.965, 122, ['drama'], 15.0, 356.296601],
    ["Shakespeare in Love", 1998, 7.452, 123, ['drama', 'melodrama', 'comedy', 'history'], 25.0, 289.317794],
    ["Titanic", 1997, 8.369, 194, ['drama', 'melodrama'], 200.0, 2185.372302],
    ["The English Patient", 1996, 7.849, 155, ['drama', 'melodrama', 'war'], 27.0, 231.976425],
    ["Braveheart", 1995, 8.283, 178, ['drama', 'war', 'biography', 'history'], 72.0, 210.409945],
    ["Forrest Gump", 1994, 8.915, 142, ['drama', 'melodrama'], 55.0, 677.386686],
    ["Schindler\'s List", 1993, 8.819, 195, ['drama', 'biography', 'history'], 22.0, 321.265768],
    ["Unforgiven", 1992, 7.858, 131, ['drama', 'western'], 14.4, 159.157447],
    ["Silence of the Lambs", 1990, 8.335, 114, ['thriller', 'crime', 'mystery', 'drama', 'horror'], 19.0, 272.742922],
    ["Dances with Wolves", 1990, 8.112, 181, ['drama', 'adventure', 'western'], 22.0, 424.208848],
    ["Driving Miss Daisy", 1989, 7.645, 99, ['drama'], 7.5, 145.793296],
    ["Rain Man", 1988, 8.25, 133, ['drama'], 25.0, 354.825435],
]


def filter_by_genre(data, genre):
    result = []
    for row in data:
        genres = row[4]
        if genre in genres:
            result.append(row)
    return result


all_genres = [
    'sci-fi', 'drama', 'crime', 'history', 'comedy', 'biography',
    'thriller', 'war', 'melodrama', 'action', 'adventure', 'western',
    'mystery', 'horror'
]

genres_counts = []
for genre in all_genres:
    # call the function filter_by genre and use len()
    count = len(filter_by_genre(oscar_data, genre))
    # use append() to add the genre name and results to the genres_counts table
    genres_counts.append([genre, count])
    


# use sort() to sort the table in descending order
genres_counts.sort(key=lambda row: row[1], reverse = True)

print('Genre        | Number')
print('------------------------')
for row in genres_counts:
    genre = row[0]
    count = row[1]
    print('{: <11} | {: >10}'.format(genre, count))