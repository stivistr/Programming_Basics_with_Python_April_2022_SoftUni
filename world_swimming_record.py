world_record = float(input())
distance_for_swim = float(input())
time_for_one_meter_swiming = float(input())

time_for_swimming_the_distance = distance_for_swim * time_for_one_meter_swiming
delay = (distance_for_swim // 15) * 12.5
whole_time = time_for_swimming_the_distance + delay

if whole_time >= world_record:
   total = whole_time - world_record
   print(f"No, he failed! He was {total:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {whole_time:.2f} seconds.")