needed_amount_of_nylon = int(input())
needed_amount_of_paint = int(input())
amount_of_thinner = int(input())
hours_of_working = int(input())

price_for_nylon = (needed_amount_of_nylon * 1.50) + 3
price_for_paint = ((needed_amount_of_paint * 14.50) * 0.10) + (needed_amount_of_paint * 14.50)
price_for_thinner = amount_of_thinner * 5
bag = 0.40
total_price_for_materials = price_for_thinner + price_for_paint + price_for_nylon + bag
total_price_for_workers_per_hour = (total_price_for_materials * 0.30) * hours_of_working

final_price_for_renovation = total_price_for_materials + total_price_for_workers_per_hour

print(final_price_for_renovation)
