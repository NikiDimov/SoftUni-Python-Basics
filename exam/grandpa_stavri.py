days = int(input())
total_degrees = 0
total_litters = 0
for day in range(days):
    litter = float(input())
    total_litters += litter
    current_degree = float(input())
    total_degrees += current_degree*litter
middle_degrees = total_degrees / total_litters

print(f"Liter: {total_litters:.2f}")
print(f"Degrees: {middle_degrees:.2f}")
if middle_degrees < 38:
    print(f"Not good, you should baking!")
elif 38 <= middle_degrees <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")
