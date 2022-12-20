import sys

n = int(input())

num_sum = 0
max_num = -sys.maxsize
for i in range(0,n):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num

    num_sum += current_num
num_sum -= max_num

if num_sum == max_num:
    print('Yes')
    print(f'Sum = {num_sum}')
else:
    diff = abs(num_sum - max_num)
    print('No')
    print(f'Diff = {diff}')