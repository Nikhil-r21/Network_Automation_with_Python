# Consider this File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/macs.txt 
# This text file that contains multiple duplicate MAC addresses.
# Create a new file('mac_unique.txt') that contains only unique MAC addresses. Each MAC should be on its own line.

with open('File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/macs.txt') as f:
    content = f.read().split()
    content = list(set(content))
    print(content)


with open('File_Processing/HandsOnChallenges_WorkingWithTextFiles/Text_Files/mac_unique.txt', 'w', newline='') as f:
    for mac in content:
        f.write(f'{mac}\n')

