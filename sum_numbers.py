number = int(input())
sum_cnt = 0

while sum_cnt < number:
    next_number = int(input())
    sum_cnt += next_number

if sum_cnt >= number:
    print(sum_cnt)