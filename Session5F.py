promo_codes = {
    'BINGO': {
        'minimum_amount': 200,
        'discount': 0.50,
        'discount_upto': 200
    },
    'JUMBO': {
        'minimum_amount': 500,
        'discount': 0.30,
        'discount_upto': 0
    }
}

amount_in_cart = int(input('Enter Amount: '))
promo_code = input('Enter Promo Code: ')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('You Entered Amount:', amount_in_cart)
print('You Entered Promo Code:', promo_code)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~')

if promo_code in promo_codes:
    print('Promo Code Valid', promo_code)
    promo_code_rule = promo_codes[promo_code]
    print(promo_code_rule, type(promo_code_rule))

    if amount_in_cart > promo_code_rule['minimum_amount']:
        discount_calculated = amount_in_cart - (promo_code_rule['discount']*amount_in_cart)
        print('discount_calculated: \u20b9', discount_calculated)

        if discount_calculated > promo_code_rule['discount_upto']:
            amount_to_pay = amount_in_cart - promo_code_rule['discount_upto']
        else:
             amount_to_pay = amount_in_cart - discount_calculated

        print('Promo Code applied successfully')
        print('Please Pay: \u20b9', amount_to_pay)

    else:
        print('Promo Code cannot be applied. Enter items worth',  promo_code_rule['minimum_amount'] - amount_in_cart, 'more')

else:
    print('Promo Code InValid')