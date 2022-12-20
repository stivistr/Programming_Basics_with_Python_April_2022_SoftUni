pens = int(input())
markers = int(input())
liters_liquid_for_cleaning = int(input())
discount_percent = int(input()) /100

price_for_pens = pens * 5.80
price_for_markers = markers * 7.20
price_for_liters_liquid_for_cleaning = liters_liquid_for_cleaning * 1.20
total_price = price_for_pens + price_for_markers + price_for_liters_liquid_for_cleaning
final_price = total_price - (total_price * discount_percent)

print(final_price)

