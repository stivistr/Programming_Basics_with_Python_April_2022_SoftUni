import sys

number = input()

max_number = -sys.maxsize

while number != 'Stop':
    number = int(number)

    if number > max_number:
        max_number = number

    number = input()

if number == 'Stop':
    print(max_number)