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
