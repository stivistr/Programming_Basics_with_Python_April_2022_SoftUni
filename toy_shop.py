holiday_price = float(input())
riddles_number = int(input())
talking_dolls_number = int(input())
teddy_bear_number = int(input())
minions_number = int(input())
trucks_number = int(input())
number_of_order = talking_dolls_number + teddy_bear_number + minions_number + trucks_number + riddles_number
discount = 0

riddle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

overall_price = (riddle_price * riddles_number) + (talking_doll_price * talking_dolls_number) + \
                (teddy_bear_price * teddy_bear_number) + (truck_price * trucks_number) + (minion_price * minions_number)

if number_of_order >= 50:
    discount = 0.25 * overall_price

final_price = overall_price - discount
money_for_rent = final_price * 0.1
final_price = final_price - money_for_rent

if final_price >= holiday_price:
    final_price -= holiday_price
    print(f"Yes! {final_price:.2f} lv left.")
elif final_price < holiday_price:
    holiday_price -= final_price
    print(f"Not enough money! {holiday_price:.2f} lv needed.")


