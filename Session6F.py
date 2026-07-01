"""
def square_of_numbers(numbers):
    print('[square_of_number] start')
    print('[square_of_number] Before', numbers, id(numbers))

    for index in range(len(numbers)):
        numbers[index] = numbers[index] * numbers[index]

    print('[square_of_number] After', numbers, id(numbers))
    print('[square_of_number] end')
    # return

"""
def square_of_numbers(numbers):
    print('[square_of_number] start')
    print('[square_of_number] Before', numbers, id(numbers))
    
    # Assignment
    # create a new list, which has a separate hashcode
    # copy all of the data into this new list
    my_numbers = []
    for index in range(len(numbers)):
       my_numbers.append(numbers[index])

    print('[square_of_number] Before', my_numbers, id(my_numbers))

    for index in range(len(my_numbers)):
        my_numbers[index] = my_numbers[index] * my_numbers[index]

    print('[square_of_number] After', my_numbers, id(my_numbers))
    print('[square_of_number] After', numbers, id(numbers))
    print('[square_of_number] end')
    # return

def main():
    print('[main] start')
    data = [10, 20, 30, 40, 50]
    print('[main] Before', data, id(data))
    square_of_numbers(data) # square_of_numbers(numbers=data)
    print('[main] After', data, id(data))
    print('[main] end')


if __name__ == '__main__':
    main()