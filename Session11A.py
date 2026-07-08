# file = open('quotes.txt', 'w') # write
file = open('quotes.txt', 'a') # append mode
quote = input('Enter a Quote: ')
file.write(quote+'\n')
file.close()
print('Quote Saved...')