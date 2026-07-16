# Iterator
# it is an object, which gives you one item at a time

# orders = ['Pizza', 'Burger', 'Pasta', 'Noodles', 'Coke']
# orders = ('Pizza', 'Burger', 'Pasta', 'Noodles', 'Coke')
# orders = {'Pizza', 'Burger', 'Pasta', 'Noodles', 'Coke'}
# orders = 'Pizza'

orders = {
    'o1': 'Pizza',
    'o2': 'Burger',
    'o3': 'Pasta',
    'o4': 'Noodles',
    'o5': 'Coke'
}

# for order in orders:
#     print(order)

orders_iterator = iter(orders)
print(orders_iterator, type(orders_iterator))

key = next(orders_iterator)
print(key, orders[key])

print(next(orders_iterator))
print(next(orders_iterator))
print(next(orders_iterator))
print(next(orders_iterator))
print(next(orders_iterator))
# print(next(orders_iterator)) # error -> StopIteration (Error)