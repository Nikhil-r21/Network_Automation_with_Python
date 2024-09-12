# Continue the previous challenge and find the 3 most frequently used letters in all English Words.

# You should get: ('e', 67681), ('s', 50872), ('i', 50818)

import string

letters = dict()

for c in string.ascii_lowercase:
    letters[c] = 0

with open('File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/american-english.txt', 'r') as words:
    for w in words:
        for char in string.ascii_lowercase:
            letters[char] += w.count(char)

print(sorted(letters.items(), key=lambda x:x[1], reverse=True))