# instagram_user_name is a REFERENCE VARIABLE
instagram_user_name = 'auribises' # Creational Statement | MODEL
age = 30

# Output Statement | VIEW
print('hashcode of instagram_user_name:', id(instagram_user_name), type(instagram_user_name))
print('hashcode of age:', id(age),  type(age))
                        # Data in Right hand Side : Literal 
instagram_user_name = 'google'
johns_age = 30

print('hashcode of instagram_user_name:', id(instagram_user_name), type(instagram_user_name))
print('hashcode of johns_age:', id(johns_age),  type(johns_age))

del johns_age
del age
# print('johns_age is:', johns_age)
print('age is:', age)