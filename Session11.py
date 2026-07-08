# file = open('Session10C.py', 'r')
# file = open('/Users/ishant/Downloads/awesome.txt', 'r')
# print(type(file))
# data = file.read()
# print(type(data))
# print(len(data))
# print(data)

# lines = file.readlines()
# file.close() # release memory resources
# print(type(lines), len(lines))

# # print(lines)

# for line in lines:
#     print(line)


with open('Session10C.py') as file:
    lines = file.readlines()
    for line in lines:
        print(line)

file.close()
print('Program Finished')

