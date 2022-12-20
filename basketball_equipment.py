charge_for_one_year_for_training = int(input())

sneakers = charge_for_one_year_for_training - (charge_for_one_year_for_training * 0.40)
kit = sneakers - (sneakers * 0.20)
ball = kit * 0.25
accessories = ball * 0.20

final_costs = charge_for_one_year_for_training + sneakers + kit + ball + accessories

print(final_costs)