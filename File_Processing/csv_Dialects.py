import csv
# with open('./File_Processing/Data/passwd.csv', 'r') as f:
#     reader = csv.reader(f, delimiter=':', lineterminator='\n')
#     for row in reader:
#         print(row)

# print(csv.list_dialects())  

csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')

with open('./File_Processing/Data/items.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='hashes')

    for row in reader:
        print(row)


with open('./File_Processing/Data/items.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='hashes')
    writer.writerow(('pencil', 3, 1.5))