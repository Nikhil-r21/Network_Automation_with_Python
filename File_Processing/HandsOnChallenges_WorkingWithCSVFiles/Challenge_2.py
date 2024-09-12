# Change the solution from the previous challenge and use : (colon) as the delimiter.

import csv

people = [
    ['Dan', 34, 'Bucuresti'],
    ['Andrei',21, 'London'],
    ['Maria', 45, 'Paris']
]


with open('File_Processing/HandsOnChallenges_WorkingWithCSVFiles/Output_Data/people2.csv', 'w') as f:
    writer = csv.writer(f, delimiter=':')
    for item in people:
        writer.writerow(item)


with open('File_Processing/HandsOnChallenges_WorkingWithCSVFiles/Output_Data/people2.csv') as f:
    reader = csv.reader(f, delimiter=':')
    for row in reader:
        print(row)