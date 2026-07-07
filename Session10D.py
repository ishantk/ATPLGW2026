customer_name = 'John'
customer_phone = '+91 98765 12345'

customer = {
    'customer_name': 'John',
    'customer_phone': '+91 98765 12345'
}

print(f'Customer Details: {customer_name} | {customer_phone}')
# print('Customer Details: {} | {}'.format(customer_name, customer_phone))
# print('Customer Details: {0} | {1}'.format(customer_name, customer_phone))
print('Customer Details: {1} | {0}'.format(customer_name, customer_phone))
print('Customer Details: {customer_name} | {customer_phone}'.format_map(customer))