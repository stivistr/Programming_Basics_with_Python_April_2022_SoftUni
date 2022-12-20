bad_marks = int(input())
task_name = input()
mark = int(input())

bad_marks_cnt = 0
number_of_tasks = 0
average_score = 0
curr_task = input()

while curr_task != 'Enough':
    average_score += mark
    number_of_tasks += 1

    task_name = input()
    mark = int(input())


