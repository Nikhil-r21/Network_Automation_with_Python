# Change the solution from the previous challenge so that the script that prints out the last n lines of the file refreshes the output every 3 seconds (as the file changes or updates). 
# This is similar to the tail -f Linux command.
# Consider this File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/sample_file_01.txt 

import time
def tail(file, n):
    with open(file, 'r') as f:

        content = f.read().splitlines()
        last = content[len(content)-n:]

        my_str = '\n'.join(last)
        return my_str

while True:
    t = tail('File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/sample_file_01.txt', 3)
    print(t)
    time.sleep(3)
    print('')
    