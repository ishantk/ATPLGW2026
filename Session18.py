import re

text = 'Python is easy to learn'

# if 'easy' in text # memebership Testing

result = re.search('easy', text)
print('result:', result)

if result:
    print('easy searched and found')
else:
    print('Cannot find easy')


text = 'Order id 101 costs 2500 inr'
result = re.findall(r"\d+", text)
print(result)

text = """
this is awesome
john@example.com we are learning regular expressions in python
admin@finlo.in
hello@gmail.com
"""

result = re.findall(r"\S+@\S+", text)
print(result)

phone = '9876512345' # exactly a 10 digit phone number
result = re.fullmatch(r"\d{10}", phone)
print(result)
if result:
    print('Phone number is OK')

pan = 'BBVPK2144K'
result = re.fullmatch(r"[A-Z]{5}[0-9]{4}[A-Z]", pan)

if result:
    print('Perfect PAN Card')

vehicle_number = 'PB10AL2937'
result = re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}", vehicle_number)
if vehicle_number:
    print('vehicle_number is OK')


text = """
i want to place a call to +919876512345 and send an email to john@example.com
as my vehicle PB10AL2937 is having a flat tyre. I need help immediately
"""
# With Regular Expression, filter 3 things -> Phone, email and Vehicle Number


text = 'Learning #python and #agenticai with #auribises'
hashtags = re.findall(r'#\w+', text)
print('hashtags:', hashtags)

text = 'Visit the site https://finlo.in to read about parking ticketing'
urls = re.findall(r'https?://\S+', text)
print('urls:', urls)
