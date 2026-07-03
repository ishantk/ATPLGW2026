"""
    data: [10, 20, 30]

    data: [10]    
    if len(data) == 1
       max -> data[0]

       
    data: [10, 20]    
    if len(data) == 1
       max -> data[0]
    else
        data[0] > data[1]
            return data[0]
        else
            returb data[1]

"""


def get_max(numbers, length):
    
    if length == 1:
        return numbers[0]
    else:
        previous = get_max(numbers, length-1)
        current = numbers[length-1]
        
        if previous > current:
            return previous
        else:
            return current


# data = [10, 20, 30]
# data = [10]
data = [10, 40, 30, 50, 20]
result = get_max(data, len(data))
print('max is:', result)

