with open('File_Processing/Data/devices.txt') as f:
    content = f.read().splitlines()
    print(content)
    devices = list()
    for line in content[1:]:
        devices.append(line.split(':'))

print(devices)

for device in devices:
    print(f"pinging {device[1]}")
