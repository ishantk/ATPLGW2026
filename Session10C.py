"""
    Strings in Python
"""

# cafe_name = 'Johns Cafe'
# cafe_name = "John's Cafe"
cafe_name = """Johns Cafe
Redwood Shores
+91 98765 12345
"""

cafe_name = 'John\'s Cafe'

print(cafe_name)

# Strings are IMMUTABLE
# they cannot be changed
# whenever you manipulate the string, you get a new string in memory
names = 'john, jennie, jim, jack, joe'
upper_case_names = names.upper() # lower, capitalize
print('names:', names, type(names), id(names))
print('upper_case_names:', upper_case_names, type(upper_case_names), id(upper_case_names))

result = names.split(', ')
print(result)

order = 'i want to order chai samosa with pakora'
keywords = order.split(' ')
print(keywords)

if 'chai' in keywords:
    print('What kind of Tea you want ?')

"""
email = input('Enter Your Email: ')
password = input('Enter Your Password: ') # length 8, upper case, lower case, special ....
print('email entered:', email)

if '@' in email and '.' in email and len(password) >8:
    print('Valid email and Valid Password')
else:
    print('InValid email or Password')
"""

vehicle_reg_number = 'PB10AL2937' # Regular Expressions (regex)
# Indexing
print(vehicle_reg_number[0])
print(vehicle_reg_number[len(vehicle_reg_number)-1])

# Negative Indexing
print(vehicle_reg_number[-1])
print(vehicle_reg_number[-2])

# Slicing
print(vehicle_reg_number[0:2])
print(vehicle_reg_number[2:4])
print(vehicle_reg_number[4:])
print(vehicle_reg_number[:5])

# Pythonic way to use slicing to reverse a string
print(vehicle_reg_number[::-1])

# String concatenation
full_name = 'John' + ' ' + 'Watson'
print(f'Full Name is: {full_name}')

line = '='*60
print(line)

# password = '   password123 '.strip()
# password = '   password123 '.lstrip()
# password = '   password123 '.rstrip()
bill_amount = '23.45000'.rstrip('0')
print(bill_amount)