pages = int(input())
pages_per_hour = int(input())
days_to_complete_a_book = int(input())
overall_time_for_book = pages / pages_per_hour
hours_per_day_for_reading = round(overall_time_for_book / days_to_complete_a_book)

print(hours_per_day_for_reading)
