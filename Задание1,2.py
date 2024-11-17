from csv import reader

print('\033[34mЗАДАНИЕ 1\033[0m')

count = 0
with open('books-en.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        if len(row[1]) > 30:  
            try:
                price = float(row[6].replace(',', '.'))  
                if price <= 150:  
                    count += 1
            except ValueError:
                print(f'Invalid price: {row[6]}')

print('Total number is: ', count)

from csv import reader

print('\033[34mЗАДАНИЕ 2\033[0m')

def search(file, author, highprice=150):
    outcome = []
    with open(file, 'r') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
            if author.lower() in row[2].lower():  
                try:
                    price = float(row[6].replace(',', '.'))
                    if price <= highprice:  
                        outcome.append(row)
                except ValueError:
                    print(f'Invalid price: {row[6]}')
    return outcome

file = 'books-en.csv'
author = input('Enter author\'s name to search: ')

result = search(file, author)

if result:
    print(f'\u001b[44mBooks by {author} at price up to 150:\u001b[0m')
    total_number_of_books = 0
    for row in result:
        print(f'Name: {row[1]}, Price: {row[6]}')
        total_number_of_books += 1
    print('Total number of books is: ', total_number_of_books)
else:
    print(f'No books found by {author} at price up to 150')
