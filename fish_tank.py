lenght_in_centimeters = int(input())
width_in_centimeters = int(input())
height_in_centimeters = int(input())
percents = float(input()) / 100

capacity_of_water_tank = lenght_in_centimeters * width_in_centimeters * height_in_centimeters
capacity_in_liters = capacity_of_water_tank / 1000
filled_space_with_other = percents
needed_liters_to_fill_the_tank = capacity_in_liters * (1 - filled_space_with_other)

print(needed_liters_to_fill_the_tank)