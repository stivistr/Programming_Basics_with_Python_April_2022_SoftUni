n = int(input())


left_sum = 0
right_sum = 0

for i in range(1, n + 1):
    left_one = int(input())
    left_two = int(input())
    left_sum = left_one + left_two

    right_one = int(input())
    right_two = int(input())
    right_sum = right_two + right_one

    if left_sum == right_sum:

    else:
        diff = abs(left_sum - right_sum)

print(f'Yes, sum = {left_sum}')
print(f'No, diff = {diff}')