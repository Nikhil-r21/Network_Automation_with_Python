# Consider this dictionary file.
# Write a Python script that reads the file in a dictionary. 
# The words in the file will be the dictionary keys and the length of each word the corresponding values.
# Consider this File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/american-english.txt 

with open('File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/american-english.txt') as f:
    words = f.read().splitlines()


    words_and_length = dict()
    for w in words:
        words_and_length[w] = len(w)

    for k, v in words_and_length.items():
        print(f'{k} -> {v}')

