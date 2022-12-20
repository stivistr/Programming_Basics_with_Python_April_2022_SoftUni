deposit_sum = float(input())
months = int(input())
year_gain_percent = float(input())
gain_per_month = ((deposit_sum * year_gain_percent) / 12) / 100
final_sum = deposit_sum + (months * gain_per_month)

print(final_sum)

