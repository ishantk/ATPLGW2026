def square_of_number(number):
    print('[square_of_number] start')
    print('[square_of_number] Before', number, id(number))
    number = number * number
    print('[square_of_number] After', number, id(number))
    print('[square_of_number] end')
    # return 


def main():
    print('[main] start')
    data = 10
    print('[main] Before', data, id(data))
    square_of_number(data) # square_of_number(number=data)
    print('[main] After', data, id(data))
    print('[main] end')


if __name__ == '__main__':
    main()