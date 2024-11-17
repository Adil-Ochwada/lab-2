print('\033[34mЗАДАНИЕ 3\033[0m')

import random
from csv import reader

def refs(file, records=20):
    references = []
    try:
        with open(file, 'r') as csvfile:
            table = list(reader(csvfile, delimiter=';'))
            
            if len(table) > 0 and not table[0][0].replace(',', '.').isdigit():
                table = table[1:]

            filtered_table = []
            for row in table:
                if len(row) > 6:  
                    try:
                        price = float(row[6].replace(',', '.'))
                        if price <= 150:  
                            filtered_table.append(row)
                    except ValueError:
                        print(f"Skipping invalid row: {row}")  

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
