# Write a Python script that compares line by line two text files and displays the lines that differ.

with open('File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/a.txt') as f:
    file1 = f.read().splitlines()

with open('File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/b.txt') as f:
    file2 = f.read().splitlines()

file = list(zip(file1, file2))

i = 0
for item in file:
    i += 1
    if item[0] != item[1]:
        print(f'file1 ({i}): {item[0]}, file2 ({i}): {item[1]}')