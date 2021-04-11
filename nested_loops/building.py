floors = int(input())
rooms = int(input())
for floor in range(floors, 0, -1):
    if floor == floors:
        type_ = "L"
    elif floor % 2 == 0:
        type_ = "O"
    else:
        type_ = "A"
    for room in range(rooms):
        print(f"{type_}{floor}{room}", end=' ')
    print()
