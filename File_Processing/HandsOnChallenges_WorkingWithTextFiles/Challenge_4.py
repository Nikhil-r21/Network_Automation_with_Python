# Create a Python function called tail that reads the last n lines of a text file. 
# The function has two arguments: the file name and n (the number of lines to read). 
# This is similar to the Linux `tail` command.

# Example: tail('sample_file.txt', 5) will return the last 5 lines from sample_file.txt.
# Consider this File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/sample_file_01.txt 

def tail(file, n):
    with open(file, 'r') as f:
        content = f.read().splitlines()
        last = content[len(content)-n:]

        my_str = '\n'.join(last)
        return my_str

t = tail('File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/sample_file_01.txt', 3)
print(t)
