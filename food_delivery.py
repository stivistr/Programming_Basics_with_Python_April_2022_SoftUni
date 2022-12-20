chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

price_for_chicken_menu = chicken_menu * 10.35
price_for_fish_menu = fish_menu * 12.40
price_for_vegan_menu = vegan_menu * 8.15
final_price = price_for_chicken_menu + price_for_vegan_menu + price_for_fish_menu
desert = final_price * 0.20
delivery_price = 2.50
total_price = final_price + desert + delivery_price


print(total_price)
