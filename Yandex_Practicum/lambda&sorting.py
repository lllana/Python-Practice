data = [
    ['Grinning', 2.26, 1.02, 87.3],
    ['Beaming', 19.1, 1.69, 150.0],
    ['ROFL', 25.6, 0.774, 0.0],
    ['Tears of Joy', 233.0, 7.31, 2270.0],
    ['Winking', 15.2, 2.36, 264.0],
    ['Happy', 22.7, 4.26, 565.0],
    ['Heart Eyes', 64.6, 11.2, 834.0],
    ['Kissing', 87.5, 5.13, 432.0],
    ['Thinking', 6.81, 0.636, 0.0],
    ['Unamused', 6.0, 0.236, 478.0],
    ['Sunglasses', 4.72, 3.93, 198.0],
    ['Loudly Crying', 24.7, 1.35, 654.0],
    ['Kiss Mark', 21.7, 2.87, 98.7],
    ['Two Hearts', 10.0, 5.69, 445.0],
    ['Heart', 118.0, 26.0, 1080.0],
    ['Heart Suit', 3.31, 1.82, 697.0],
    ['Thumbs Up', 23.1, 3.75, 227.0],
    ['Shrugging', 1.74, 0.11, 0.0],
    ['Fire', 4.5, 2.49, 150.0],
    ['Recycle', 0.0333, 0.056, 932.0]
]

for i in range(len(data)):
    total = data[i][1] + data[i][2] + data[i][3]  
    data[i].append(total)

data.sort(key=lambda row: row[4], reverse=True)

print("Emoji name       | Total usage, mil.")
print("-----------------------------------------------")
for row in data[:5]:
    print('{: <16} | {: >28.2f}'.format(row[0], row[4]))