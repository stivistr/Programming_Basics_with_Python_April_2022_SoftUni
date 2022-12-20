budget_for_filming = float(input())
extras = int(input())
extras_outfit_price = float(input())
background_price = 0.1 * budget_for_filming

if extras > 150:
    extras_outfit_price = extras_outfit_price - (extras_outfit_price * 0.1)

extras_outfit_price_overall = extras_outfit_price * extras
needed_money_for_filming = extras_outfit_price_overall + background_price

if needed_money_for_filming > budget_for_filming:
    total = (budget_for_filming - needed_money_for_filming) * -1
    print("Not enough money!")
    print(f"Wingard needs {total:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget_for_filming - needed_money_for_filming:.2f} leva left.")
