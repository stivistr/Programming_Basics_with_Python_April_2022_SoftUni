income = input()
total_money = 0

while income != 'NoMoreMoney':
    income = float(income)

    if income < 0:
        print('Invalid operation!')
        print(f'Total: {total_money:.2f}')
        break

    print(f'Increase: {income:.2f}')
    total_money += income
    income = input()


if income == 'NoMoreMoney':
    print(f'Total: {total_money:.2f}')

