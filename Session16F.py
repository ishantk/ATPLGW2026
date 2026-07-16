from functools import reduce

product_prices = [100, 300, 450, 120, 900]
discounted_prices = []

discount = lambda price, percentage : price * percentage

for price in product_prices:
    discounted_prices.append(discount(price, 0.50))

print('product_prices:', product_prices)
print('discounted_prices:', discounted_prices)

new_prices = list(map(lambda price: price*0.50, product_prices))
print('new_prices:', new_prices)

filtered_prices = list(filter(lambda price: price>200, product_prices))
print('filtered_prices:', filtered_prices)

total = reduce(lambda x, y : x+y, product_prices)
print('total:', total)

# Assignment: list of flights dictionary 
# lambdas -> map, filter and reduce
