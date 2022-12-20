import math
from math import ceil

tvshow_name = (input())
episode_lenght = int(input())
break_lenght = int(input())

lunch_break = break_lenght * 1/8
chill_time = break_lenght * 1/4
break_lenght -= (lunch_break + chill_time)

if break_lenght >= episode_lenght:
    break_lenght = math.ceil(break_lenght - episode_lenght)
    print(f"You have enough time to watch {tvshow_name} and left with {break_lenght} minutes free time.")
else:
    episode_lenght = math.ceil(episode_lenght - break_lenght)
    print(f"You don't have enough time to watch {tvshow_name}, you need {episode_lenght} more minutes.")