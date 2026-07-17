numbers = list(range(10, 101, 10))
print('numbers', numbers)

numbers.append(99)
numbers.append(77)
numbers.append(101)

numbers.insert(3, 33)

print('numbers', numbers)

print('sum of numbers:', sum(numbers))
print('min of numbers:', min(numbers))
print('max of numbers:', max(numbers))
print('len of numbers:', len(numbers))
print('avg of numbers:', sum(numbers) / len(numbers))

# data = tuple(numbers)
# data = set(numbers)
# data = str(numbers)
# data = dict(numbers) : error
# print('data:', data, type(data))

reverse_numbers = list(reversed(numbers))
print('reverse_numbers:', reverse_numbers)

# Python - reverse with slicing technique
print(numbers[::-1])

# numbers.sort(reverse=True)
numbers.sort()
print(numbers)

index = numbers.index(101)
print('index of 101:', index)

numbers.remove(99)
del numbers[6]
numbers.clear()
# del numbers

data = [10, 20, 30, 40, 50]
print('before data:', data)
# data.append(70)
data.pop()
print('after data:', data)

# Assignment: Explore queue implementation on list