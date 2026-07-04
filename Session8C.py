"""
    1. Think of Object
    User: name, phone, email, age, gender, address

    2. Create its class (Representation)

"""

class User:
    # constructor function in User
    # self is a reference variable, which holds the hashcode of current object
    def __init__(self, kuchbhi, phone, email, age, gender, address):
        print('[LOG] __init__ | self', self, type(self))
        # LHS: self.name means we are creating attribute in Object
        # RHS kuchbhi will have the value for the attribute
        self.name = kuchbhi
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender
        self.address = address

    # redefining the contructor removes the old definition of contructor from memory
    # we dont have overloading in python
    # def __init__(self, name):
        # pass

# 3. Create real object in memory
# Object Constrcution Statement

user1 = User(kuchbhi='John', 
             phone='+91 99990 11110', 
             email='john@example.com',
             age=20,
             gender='male',
             address='redwood shores')

user2 = User(kuchbhi='Fionna', 
             phone='+91 99991 11111', 
             email='fionna@example.com',
             age=21,
             gender='female',
             address='country homes')

user3 = user1

del user3.address
user1.status = 'online'


print('user1:', user1, vars(user1))
print('user2:', user2, vars(user2))
print('user3:', user3, vars(user3))