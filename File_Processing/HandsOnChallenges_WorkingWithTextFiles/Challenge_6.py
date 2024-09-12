# Write a Python program to count the number of lines, words, and characters in a text file. 
# This is similar to the Linux `wc` command. Create a function, if possible.
# Consider this File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/sample_file_01.txt 

def wc(file):
    with open(file, 'r') as f:
        content = f.read().splitlines()

        lines = len(content)

        words = 0
        for line in content:
            words += len(line.split())

        chars = 0
        for line in content:
            chars += len(list(line))

        return lines, words, chars

print(wc('File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/sample_file_01.txt'))