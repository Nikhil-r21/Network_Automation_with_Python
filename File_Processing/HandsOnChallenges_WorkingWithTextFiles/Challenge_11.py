# Consider the previous dictionary file.
# Write a Python script that finds the number of occurrences of each letter of the alphabet in all the words of the dictionary. 
# Make a distinction between lower and uppercase letters.
# You want to see how many times 'a', 'A', 'b', 'B', 'c', 'C', 'd' and so on appear in all the words in the dictionary.
# Which is the most frequently used letter in English words? But the least frequently used one?

import string

letters = dict()

for c in string.ascii_letters:
    letters[c] = 0


with open('File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/american-english.txt', 'r') as words:
    for w in words:
        for char in string.ascii_letters:
            letters[char] += w.count(char)

print(letters)
