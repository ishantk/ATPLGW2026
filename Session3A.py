# Single Value Container
a = 10
b = a  # Reference Copy Operation

# Multi Value Container
data = [10, 20, 30, 40, 50]
data = [10, 20, 30, 40, 50]
numbers = data # Reference Copy Operation

numbers[2] = 1000

print("a:", a, id(a))
print("b:", b, id(b))

print("data:", data, id(data))
print('numbers:', numbers, id(numbers))