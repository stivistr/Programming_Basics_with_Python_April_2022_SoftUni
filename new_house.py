flower_type = input()
flower_count = int(input())
budget = int(input())

price_for_one_flower = 0
discount_in_price = 0
increase_in_price = 0

if flower_type == 'Roses':
    price_for_one_flower = 5
    if flower_count > 80:
        discount_in_price = 0.1
elif flower_type == 'Dahlias':
    price_for_one_flower = 3.80
    if flower_count > 90:
        discount_in_price = 0.15
elif flower_type == 'Tulips':
    price_for_one_flower = 2.80
    if flower_count > 80:
        discount_in_price = 0.15
elif flower_type == 'Narcissus':
    price_for_one_flower = 3
    if flower_count < 120:
        increase_in_price = 0.15
elif flower_type == 'Gladiolus':
    price_for_one_flower = 2.50
    if flower_count < 80:
        increase_in_price = 0.2

price = flower_count * price_for_one_flower
price -= price * discount_in_price
price += price * increase_in_price

if budget >= price:
    budget = budget - price
    print(f'Hey, you have a great garden with {flower_count} {flower_type} and {budget:.2f} leva left.')
else:
    price = price - budget
    print(f'Not enough money, you need {price:.2f} leva more.')
