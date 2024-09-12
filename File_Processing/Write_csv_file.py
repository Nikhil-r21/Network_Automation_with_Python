import csv

with open('File_Processing/Data/people.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    csvdata = (5, 'Luffy', 'Tokyo')
    writer.writerow(csvdata)


with open('File_Processing/Data/numbers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'x**2', 'x**3', 'x**4'])
    for x in range(1, 101):
        writer.writerow([x, x**2, x**3, x**4])

