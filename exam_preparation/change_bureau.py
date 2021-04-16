bit_coin_to_eur = 1168 / 1.95
chinese_money_to_eur = 0.15 * 1.76 / 1.95
total_bitcoins = int(input())
total_chinese_money = float(input())
commission = float(input())
result = total_bitcoins*bit_coin_to_eur + total_chinese_money*chinese_money_to_eur
print(f"{result - (result * commission/100):.2f}")