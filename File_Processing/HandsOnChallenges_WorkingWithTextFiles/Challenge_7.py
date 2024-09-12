# Write a Python program that calculates the net amount of a bank account based on the transactions that are saved in a text file.
# The file format is as follows:
# D:50
# W:100
# D means deposit while W means withdrawal.
# Suppose that the following file(File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/banking.txt) is supplied to the program:
# D:300
# D:300
# W:500
# D:200
# Then, the output should be: 300



with open('File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/banking.txt', 'r') as f:
    content = f.read().splitlines()


    deposit, withdrawal = 0, 0

    for item in content:
        tmp = item.split(':')

        if  tmp[0] == 'D':
            deposit += int(tmp[1])
        elif tmp[0] == 'W':
            withdrawal += int(tmp[1])
        else:
            print('File format error')

    balance = deposit - withdrawal
    print(balance)
