"""
    1. Think of Object
    User: name, phone, email, age, gender, address

    2. Create its class (Representation)

"""

class User:
    # constructor function in User
    # self is a reference variable, which holds the hashcode of current object
    def __init__(self):
        print('[LOG] __init__ | self', self, type(self))

# 3. Create real object in memory
# Object Constrcution Statement
# LHS: user1 is a Reference Variable which has hashcode of the Object
#      it is created in Stack
# RHS: represents the Object i.e. Container construction in Heap
#      empty object, whose hashcode will be returned to the reference variable
user1 = User()
user2 = User()

user3 = user1 
# reference copy operation
# user1 and user3 are 2 RVs pointing to the same object

user1.name = 'John'
user2.full_name = 'Fionna Flynn'
user3.age = 20
user2.age = 25
user3.email = 'john@example.com'

print(user1, vars(user1))
print(user2, vars(user2))
print(user3, vars(user3))