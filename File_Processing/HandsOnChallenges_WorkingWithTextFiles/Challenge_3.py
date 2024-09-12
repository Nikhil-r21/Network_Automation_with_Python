# Consider this File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/file.txt 
# Create a Python script that removes all empty lines including those that contain only spaces from a file.
# Create a new file('file_without_blanks.txt')

with open('File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/file.txt') as f:
    content_list = f.readlines()


tmp_list = [line for line in content_list if line.strip() != '']
print(tmp_list)

with open('File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/file_without_blanks.txt', 'w') as f:
    f.write(''.join(tmp_list))

