position = [
['2019-05-01', '- 6'],
['2019-05-02', '+5'],
['2019-05-03', ' 5'],
['2019-05-04', '4'],
['2019-05-05', '5'],
['2019-05-06', '5'],
['2019-05-07', '4'],
['2019-05-08', 'Error 5'],
['2019-05-09', '3'],
['2019-05-10', '3'],
]

total_position = 0
count_rows = 0
erroneous_rows = 0

for row in position:
    count_rows += 1
    try:
        level = int(row[1])
        total_position += level
    except:
        erroneous_rows += 1

print('Total measurements',count_rows)
print('Total erroneous rows',erroneous_rows)