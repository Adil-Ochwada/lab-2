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
