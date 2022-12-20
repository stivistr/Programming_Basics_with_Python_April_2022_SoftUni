exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_total_time = exam_hour * 60 + exam_minutes
arrival_total_time = arrival_hour * 60 + arrival_minutes
time_diff = abs(exam_total_time - arrival_total_time)


if arrival_total_time > exam_total_time:
    print('Late')
    if time_diff >= 60:
        hours_late = time_diff // 60
        minutes_late = time_diff % 60
        print(f'{hours_late}:{minutes_late:02d} hours after the start')
    else:
        print(f'{time_diff:02d} minutes after the start')
elif arrival_total_time <= exam_total_time and time_diff <=30:
    print('On time')
    if time_diff > 0:
        print(f'{time_diff} minutes before the start')
else:
    print('Early')
    if time_diff >= 60:
        hours_early = time_diff // 60
        minutes_early = time_diff % 60
        print(f'{hours_early}:{minutes_early:02d} hours before the start')
    else:
        print(f'{time_diff} minutes before the start')
