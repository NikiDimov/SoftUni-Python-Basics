l = int(input())
b = int(input())
h = int(input())
occupied_volume = float(input())
fish_tank_volume_sm = l * b * h
one_liter_sm = 0.001

fish_tank_liter = fish_tank_volume_sm * one_liter_sm
result = fish_tank_liter - (fish_tank_liter * (occupied_volume/100))
print(result)
