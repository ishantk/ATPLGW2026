"""

    multi value container
    Sequeunces (which works on indexing)
        tuple
        list
        string


        other multi value container
        set     - hashing
        dictionary - key value pair, where keys are hashed

        
    Properties:
        1. Indexing
        2. Negative Indexing
        3. Slicing
        4. Concatenation
        5. Multiplicity
        6. Membership Testing
"""

# Indexing
# Negative Indexing

#           0.  1.  2.  3.  4. 
#           -5. -4. -3. -2. -1
my_data = [10, 20, 30, 40, 50]
print(my_data[0])       # 10
print(my_data[-1])      # 50
print(my_data[-5])      # 50

# CRASH -> wherever erro occurs, the next part of program will not be executed
# Unfortunately, Application has Stopped Working
# Handling Run Time Errors, so my program should not CRASH
try:
    print(my_data[7])       # Error at Run Time
except:
    print('Something went wrong')

print('Last Statement')

# 2-D List -> List of 1D Lists
numbers = [
    [10, 20, 30],       # 0
    [40, 50, 60],       # 1
    [70, 80, 90],       # 2
]

print('len(numbers):', len(numbers))
print('len(numbers[0]):', len(numbers[0]))

print(numbers[0][2]) # 2
print(numbers[-1])
print(numbers[-1][-2])

# 3D List - List of List of Lists
large_data = [
    [
        [10, 20, 30],       # 0
        [40, 50, 60],       # 1         0       -2
        [70, 80, 90],       # 2
    ],
    [
        [11, 22, 33],       # 0
        [44, 55, 66],       # 1         1       -1
        [77, 88, 99],       # 2
    ],
    [
        [11, 22, 33],
        [11, 22],
    ]
]

print('len(large_data):', len(large_data)) # 2
print('len(large_data[0]):', len(large_data[0])) # 3
print(large_data[0][2])    # [70, 80, 90]     
print(large_data[-1])
print(large_data[-1][-2])   # [44, 55, 66]
print(large_data[-2][-2][-2]) # 50


# Use Case
punjab_population = [120909, 129848, 28848]
himachal_population = [120909, 129848, 28848, 367364]
haryana_population = [120909, 129848, 28848]

india_population = [
    [punjab_population, himachal_population, haryana_population]
]

world_population = [

]

# Slicing

# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
data = list(range(10, 101, 10))
print('data:', data)

print('data[2:5]', data[2:5]) # start from 2, less than 5 i.e. 4
print('data[:5]', data[:5])
print('data[5:]', data[5:])
print('data[:-5]', data[: -5]) # [10, 20, 30, 40, 50]
print('data[:-5]', data[-5 : -2]) # [60, 70, 80]

# Concatenation

data1 = [10, 20, 30]
data2 = [40, 50, 60]

data3 = data1 + data2
print('data3:', data3)

# Multiplicity
data4 = [10, 20, 30]
data5 = data4 * 3
print('data5:', data5)

# Membership Testing - for all
print(10 in data4)
print(100 in data4)
print(100 not in data4)

data6 = {10, 20, 30}
print(10 in data6)

product = {
    'code': 101,
    'name': 'Adidas Ultraboost',
    'price':  8000
}

print('price' in product) # works on key
print(8000 in product)  # will not work for value