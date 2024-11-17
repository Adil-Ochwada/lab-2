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

print('\033[34mЗАДАНИЕ 3\033[0m')

import random
from csv import reader

def refs(file, records=20):
    references = []
    try:
        with open(file, 'r') as csvfile:
            table = list(reader(csvfile, delimiter=';'))
            filtered_table = [row for row in table if len(row) > 6 and float(row[6].replace(',', '.')) <= 150]  
            data = random.sample(filtered_table, min(records, len(filtered_table)))  
            for row in data:
                author = row[2] if len(row) > 2 else "Unknown Author"
                title = row[1] if len(row) > 1 else "Unknown Title"
                year = row[4] if len(row) > 4 else "Unknown Year"
                reference = f"{author}. {title} - {year}"
                references.append(reference)
        with open('bibliographic_references.txt', 'w') as output_file:
            for i, ref in enumerate(references, 1):
                output_file.write(f"{i}. {ref}\n")
        print("Bibliographic references saved to bibliographic_references.txt.")
    except FileNotFoundError:
        print("The specified CSV file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

refs('books-en.csv')

print('\033[34mЗАДАНИЕ 4\033[0m')

import csv

def topbooks(file):
    publishers = set()
    books = []

    try:
        with open(file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                if len(row) < 7:
                    continue
                isbn, title, author, year, publisher, downloads, price = row
                try:
                    price = float(price.replace(',', '.'))
                    if price <= 150:  
                        publishers.add(publisher)
                        downloads_count = int(downloads)
                        books.append((title, author, publisher, downloads_count))
                except ValueError:
                    print(f"Invalid value in row: {row}")
        book_list = sorted(books, key=lambda x: x[3], reverse=True)[:20]

        print("Publishers:")
        for publisher in sorted(publishers):
            print(publisher)

        print("\nTop 20 Most Popular Books (by Downloads):")
        for book in book_list:
            print(f"Title: {book[0]}, Author: {book[1]}, Publisher: {book[2]}, Downloads: {book[3]}")
    except FileNotFoundError:
        print("CSV file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

topbooks('books-en.csv')

print('\033[34mЗАДАНИЕ 5\033[0m')

import xml.etree.ElementTree as ET

def operation(file):
    tree = ET.parse(file)
    root = tree.getroot()
    
    name_value_dict = {}
    for currency in root.findall('Valute'):
        name = currency.find('Name').text
        value = currency.find('Value').text
        if name and value:
            name_value_dict[name] = float(value.replace(',', '.'))  
    
    return name_value_dict

file = 'currency.xml'
name_value_dict = operation(file)

print("Name - Value Dictionary:")
for name, value in name_value_dict.items():
    print(f"{name}: {value}")
