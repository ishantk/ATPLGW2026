product = {
    'code': 101,
    'name': 'Ultraboost',
    'brand': 'Adidas',
    'price': 8000,
    'category': 'shoe'
}

print(product, type(product), id(product))
print(product['code'], type(product['code']), id(product['code']))
print(product['category'], type(product['category']), id(product['category']))
print(product['brand'], type(product['brand']), id(product['brand']))

shoe_name = 'Adidas'
print(shoe_name, type(shoe_name), id(shoe_name))

product['price'] = 7000

for key in product:
    print(key, product[key])