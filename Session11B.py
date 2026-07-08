"""
    Read the file Session10B.py
    Analyze and count the objects in file
    Write the objects in a file named objectanalysis.csv or objectanalysis.txt
    Vehicle,5
    FastTag,5
    TollPlazaQueue,1
"""

objects = {
    'Vehicle': 0,
    'FastTag': 0,
    'TollPlazaQueue': 0
}

file = open('Session10B.py', 'r')
lines = file.readlines()

for line in lines:
    pass


with open('objectanalysis.csv', 'a') as file:
    for key in objects:
        data = f'{key},{objects[key]}\n'
        file.write(data)