# Consider this File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/sample_file.txt 
# Create a Python script that reads a text file into a list and then converts the list into a string that has the entire file content.

with open('File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/sample_file.txt', 'r') as f:
    content = f.read().splitlines()
    my_str = '\n'.join(content)
    print(my_str)