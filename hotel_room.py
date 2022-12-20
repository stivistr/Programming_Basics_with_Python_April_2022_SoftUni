month = input()
nights_count = int(input())

discount = 0
price_for_apartment = 0
price_for_studio = 0
type_of_room = 'Studio' or 'Apartment'

if month == 'May' or month == 'October':
    price_for_studio = 50
    price_for_apartment = 65
    if nights_count > 7 and type_of_room == 'Studio':
       discount = 0.05
    elif nights_count > 14 and type_of_room == 'Studio':
        discount = 0.3
    else:
        var = type_of_room == 'Apartment' and nights_count >14:
        discount = 0.1

elif month == 'June' or month == 'September':
    price_for_studio = 75.20
    price_for_apartment = 68.70
    if nights_count > 14 and type_of_room == 'Studio':
        discount = 0.2
elif month == 'July' or month == 'August':
    price_for_studio = 76
    price_for_apartment = 77