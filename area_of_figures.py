from math import pi

figure = str(input())
area = 0

if figure == 'square':
    a = float(input())
    area = a * a
    print(f'{area:.3f}')
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
    print(f'{area:.3f}')
elif figure == 'circle':
    a = float(input())
    area = pi * (a ** 2)
    print(f'{area:.3f}')
elif figure == 'triangle':
    a = float(input())
    b = float(input())
    area = 1 / 2 * a * b
    print(f'{area:.3f}')


