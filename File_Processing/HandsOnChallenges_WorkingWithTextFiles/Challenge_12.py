# Change the solution from the previous challenge(Challenge_11) so that the script considers all letters lowercase (it makes no distinction between lower and uppercase letters).

import string

letters = dict()

for c in string.ascii_lowercase:
    letters[c] = 0


with open('File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/american-english.txt', 'r') as words:
    for w in words:
        for char in string.ascii_lowercase:
            letters[char] += w.lower().count(char) 

print(letters)



