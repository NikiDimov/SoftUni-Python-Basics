price_for_trip = float(input())
total_puzzles = int(input())
total_dolls = int(input())
total_teddies = int(input())
total_minions = int(input())
total_trucks = int(input())

total_toys = total_trucks + total_teddies + total_dolls + total_minions + total_puzzles
total_prize = total_trucks * 2 + total_teddies * 4.1 + total_dolls * 3 + total_minions * 8.2 + total_puzzles * 2.6

if total_toys >= 50:
    total_prize -= total_prize * 0.25

total_prize -= total_prize * 0.1

if total_prize >= price_for_trip:
    print(f"Yes! {total_prize - price_for_trip:.2f} lv left.")
else:
    print(f"Not enough money! {price_for_trip - total_prize:.2f} lv needed.")
