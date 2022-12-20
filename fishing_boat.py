budget = int(input())
season = input()
fishers_count = int(input())

additional_discount = 0
discount = 0
rent_for_boat = 0

if season == 'Spring':
    rent_for_boat = 3000
    if fishers_count <= 6:
        discount = 0.1
    elif 7 < fishers_count <= 11:
        discount = 0.15
    else:
        discount = 0.25
elif season == 'Summer' or season == 'Autumn':
    rent_for_boat = 4200
    if fishers_count <= 6:
        discount = 0.1
    elif 7 < fishers_count <= 11:
        discount = 0.15
    else:
        discount = 0.25
elif season == 'Winter':
    rent_for_boat = 2600
    if fishers_count <= 6:
        discount = 0.1
    elif 7 < fishers_count <= 11:
        discount = 0.15
    else:
        discount = 0.25

rent_for_boat -= rent_for_boat * discount

if fishers_count % 2 == 0 and season != 'Autumn':
    additional_discount = 0.05
    rent_for_boat -= rent_for_boat * additional_discount

if budget >= rent_for_boat:
    budget = budget - rent_for_boat
    print(f'Yes! You have {budget:.2f} leva left.')
else:
    rent_for_boat = rent_for_boat - budget
    print(f'Not enough money! You need {rent_for_boat:.2f} leva.')
