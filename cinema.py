type_show = input()
rows = int(input())
columns = int(input())
profit = 0

all_seats = rows * columns

if type_show == 'Premiere':
    profit = all_seats * 12
elif type_show == 'Normal':
    profit = all_seats * 7.50
else:
    profit = all_seats * 5

print(f'{profit:.2f}')