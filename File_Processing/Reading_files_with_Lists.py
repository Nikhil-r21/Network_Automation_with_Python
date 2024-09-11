##### 1. Opening and reading the file using splitlines() #####

with open('./File_Processing/Data/configuration.txt') as f:
    content = f.read().splitlines()
    print(content)
    print('#' * 50)




##### 2. Using readlines() to read file line-by-line and store in a list #####

with open('./File_Processing/Data/configuration.txt') as f:
    content = f.readlines()  
    print(content)
    print('#' * 50)




##### 3. Combining readlines() and readline() #####

with open('./File_Processing/Data/configuration.txt') as f:
    print(f.readlines())  
    print(f.readline())  # Attempts to read one line, but will not work after readlines() since the file is already fully read
    print('#' * 50)




##### 4. Converting the file contents to a list #####

with open('./File_Processing/Data/configuration.txt') as f:
    content = list(f)  # Converts the file object into a list of lines
    print(content)
    print('#' * 50)




##### 5. Iterating over the file lines directly #####

with open('./File_Processing/Data/configuration.txt') as f:
    for line in f:  # Iterates over the file line by line
        print(line, end='')  # Prints each line without adding extra newlines



