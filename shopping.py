budget = float(input())
graphic_card = int(input())
cpu = int(input())
ram_count = int(input())
discount = 0

graphic_card_price = graphic_card * 250
cpu_price = (graphic_card_price * 0.35) * cpu
ram_price = (graphic_card_price * 0.1) * ram_count
final_sum = graphic_card_price + cpu_price + ram_price

if graphic_card > cpu:
    discount = final_sum * 0.15
    final_sum -= discount

if final_sum <= budget:
    budget -= final_sum
    print(f"You have {budget:.2f} leva left!")
else:
    final_sum -= budget
    print(f"Not enough money! You need {final_sum:.2f} leva more!")