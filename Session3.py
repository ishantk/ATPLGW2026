# Single Value Container
a = 10
b = 10

# Multi Value Container
data = [10, 20, 30, 40, 50]
numbers = [10, 20, 30, 40, 50]

print("a:", a, id(a))
print("b:", b, id(b))

print("data:", data, id(data))
print('numbers:', numbers, id(numbers))

print("[0]", data[0], id(data[0]), numbers[0], id(numbers[0]))
data[1] = 100

print(data)
print(numbers)