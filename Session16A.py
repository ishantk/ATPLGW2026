# Generator - is a way to create an iterator in a function
def deliver_orders():
    yield 'Pizza'
    yield 'Burger'
    yield 'Noodles'

orders = deliver_orders()
print(orders, type(orders))

# print(next(orders))
# print(next(orders))
# print(next(orders))
# print(next(orders))

for order in orders:
    print(order)

# Try yielding, list, string, set, tuple, dictionary and then see the code working