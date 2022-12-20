budget = float(input())
season = input()

destination = ''

if budget <= 100:
    destination = 'Bulgaria'
    print(f'Somewhere in {destination}')
    if season == 'summer':
        budget = budget * 0.3
        print(f'Camp - {budget:.2f}')
    elif season == 'winter':
        budget = budget * 0.7
        print(f'Hotel - {budget:.2f}')
elif 100 < budget <= 1000:
    destination = 'Balkans'
    print(f'Somewhere in {destination}')
    if season == 'summer':
        budget = budget * 0.4
        print(f'Camp - {budget:.2f}')
    elif season == 'winter':
        budget = budget * 0.8
        print(f'Hotel - {budget:.2f}')
else:
    destination = 'Europe'
    print(f'Somewhere in {destination}')
    budget = budget * 0.9
    print(f'Hotel - {budget:.2f}')
