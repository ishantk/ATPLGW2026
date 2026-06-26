"""
john_physics = 70
john_chemistry = 80
john_maths = 85

fionna_physics = 75
fionna_chemistry = 90
fionna_maths = 95

john_marks = [70, 80, 85]
fionna_marks = [75, 90, 95]

# List of Lists
class_marks = [
    [70, 80, 85],
    [75, 90, 95]
]
"""

"""
#              0.  1.  2.  3.   4.   5. 
john_marks = [70, 80, 85, 'B', 'A', 'A']
print(john_marks, id(john_marks), type(john_marks))

print(len(john_marks))

# Output
print(john_marks[0], id(john_marks[0]), type(john_marks[0]))
print(john_marks[1], id(john_marks[1]), type(john_marks[1]))
print(john_marks[2], id(john_marks[2]), type(john_marks[2]))
print(john_marks[3], id(john_marks[3]), type(john_marks[3]))
print(john_marks[4], id(john_marks[4]), type(john_marks[4]))
print(john_marks[5], id(john_marks[5]), type(john_marks[5]))

john_marks[1] = 'B'
print(john_marks[1], id(john_marks[1]), type(john_marks[1]))

"""
# TUPLE -> IMMUTABLE -> You cannot modify the content | READ ONLY
# LIST -> MUTABLE -> You can modify the content 

            # 0.  1.  2. 
# john_marks = 70, 80, 85
john_marks = (70, 80, 85)
# john_marks = [70, 80, 85]
print('john_marks: ', john_marks, id(john_marks), type(john_marks))
# john_marks[0] = 75