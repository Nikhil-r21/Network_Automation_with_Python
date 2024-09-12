##### METHOD 1 #####
with open('./File_Processing/Data/device.txt', 'r') as f:
    device = f.read().splitlines()
    # print(device)

my_list = list()
for item in device:
    tmp = item.split(':')
    my_list.append(tmp)

print(my_list)



##### METHOD 2 #####
import csv
with open('./File_Processing/Data/device.txt', 'r') as f:
    reader = csv.reader(f, delimiter=':')
    my_list = list()
    for row in reader:
        my_list.append(row)

print(my_list)

