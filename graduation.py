name = input()

grades = 0
overall_mark = 0
failed_years = 0

while True:
    mark = float(input())
    grades += 1

    if mark < 4:
        failed_years += 1

        if failed_years == 2:
            print(f'{name} has been excluded at {grades} grade')
            break

        grades -= 1

    else:
        overall_mark += mark

    if grades == 12:
        overall_mark = overall_mark / 12
        print(f'{name} graduated. Average grade: {overall_mark:.2f}')
        break