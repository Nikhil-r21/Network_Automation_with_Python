##### 1. Reading with read(), tell(), and seek() #####

f = open('./File_Processing/Data/configuration.txt', 'rt')
content = f.read()
f.seek(0)  # Reset the file pointer to the beginning
content = f.read(19)  # Now it reads the first 19 characters
print(content)

# Get the current position in the file
print(f.tell())

# Move the file pointer to position 2
f.seek(2)

# Read the next 3 characters starting from position 2
content = f.read(3)
print(content)

f.close()





##### 2. Using seek() to read the file multiple times #####

f = open('./File_Processing/Data/configuration.txt', 'r')
print(f.read())
print("#" * 50)

f.seek(0)

print(f.read())
f.close()





##### 3. Using with open() and checking if the file is closed #####

with open('./File_Processing/Data/configuration.txt') as file:
    content = file.read() 
    print(content)

print(file.closed)



