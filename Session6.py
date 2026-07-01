data = [10, 20, 50, 70, 30, 15]
scores = [27, 110, 35, 89, 20, 30]
prices = [1500, 3000, 5000, 1200, 4500]

# Function: piece of code which contains logic(contorller), that can be reused
#           logic which needs to be executed again and again

"""
max = data[0]
for index in range(1, len(data)):
    if data[index] > max:
        max = data[index]

print('max in data is:', max)

max = scores[0]
for index in range(1, len(scores)):
    if scores[index] > max:
        max = scores[index]

print('max in scores is:', max)

max = prices[0]
for index in range(1, len(prices)):
    if prices[index] > max:
        max = prices[index]

print('max in prices is:', max)
"""


def find_max(numbers):
    max = numbers[0]
    for index in range(1, len(numbers)):
        if numbers[index] > max:
            max = numbers[index]

    print('max in', numbers, 'is:', max)


find_max(numbers=data)
find_max(numbers=scores)
find_max(numbers=prices)
find_max(prices)
find_max([11, 17, 25, 19, 33])