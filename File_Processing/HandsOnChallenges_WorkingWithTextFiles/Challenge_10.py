# Consider the dictionary file from the previous challenge.

# Write a Python script that finds the first 100 longest words in the file.

# Tip: See how to get a sorted view of a dictionary.(dict_sort_by_value.py)



with open('File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/american-english.txt') as f:
    words = f.read().splitlines()


    words_and_length = dict()
    for w in words:
        words_and_length[w] = len(w)

    # print(words_and_length)

    words_list = sorted(words_and_length.items(), key=lambda x:x[1], reverse=True)
    print(words_list[:100])