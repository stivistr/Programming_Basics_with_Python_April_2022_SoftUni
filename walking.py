steps_cnt = 0

curr_command = input()

while curr_command != 'Going home':
    steps = int(curr_command)
    steps_cnt += steps

    if steps_cnt >= 10000:
        break

    curr_command = input()

if curr_command == 'Going home':
    steps_going_home = int(input())
    steps_cnt += steps_going_home

if steps_cnt >= 10000:
    step_diff = steps_cnt - 10000
    print('Goal reached! Good job!')
    print(f'{step_diff} steps over the goal!')
else:
    steps_more_needed = 10000 - steps_cnt
    print(f'{steps_more_needed} more steps to reach goal.')

