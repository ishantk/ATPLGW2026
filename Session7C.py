# https://visualgo.net/en/sorting
# Algo: Bubble Sort

def sort(data):
    for i in range(len(data)):
        for j in range(len(data) - 1 - i):
            print('[LOG] i:', i, 'j', j, '|' ,'data[j]', data[j], 'data[j+1]', data[j+1])
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                print('[LOG] >> SWAP: data[j]', data[j], 'data[j+1]', data[j+1])


numbers = [10, 30, 20, 5, 15]

"""
i: 0, 1, 2, 3, 4

i: 0
j: 0 1 2 3

i: 1
j: 0 1 2 

.
...
.......


"""

sort(numbers)
print("numbers:", numbers)