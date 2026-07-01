# Functions in Python
# def add_numbers(number1, number2):
# def add_numbers(number1, number2=10):
# def add_numbers(number1=10, number2): # error
def add_numbers(number1=10, number2=20):
    result = number1 + number2
    print('result is:', result)


print(add_numbers)
print(hex(id(add_numbers)), type(add_numbers))


add_numbers(10, 20)
add_numbers(number1=100, number2=200)
add_numbers(number2=110, number1=40)

add_numbers()
add_numbers(10)

# Reference Copy Operation
add = add_numbers
print(add)
add(100, 200)

"""
You can delete the function also
del add
del add_numbers

add_numbers(10)
"""
