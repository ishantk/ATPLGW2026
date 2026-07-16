# Decorator: a decorator is a function, 
# which adds additional functionality to an exiting function
# without changing its behaviour

"""
def place_order():
    print('[LOG] Order Processing Started...')
    print('Order Placed Successfully...')
    print('[LOG] Order Processing Finished...')


place_order()
"""

# Technical Structure of a decorator
# Decorator is a fucntion, which takes function as input argument
# It has a nested function
# It return the nested function

def logger(func):
    
    # Nested function has to be returned
    def wrapper():
        print('[LOG] Order Processing Started...')
        func()
        print('[LOG] Order Processing Finished...')
    
    return wrapper


@logger
def place_order():
    print('Order Placed Successfully...')

place_order()