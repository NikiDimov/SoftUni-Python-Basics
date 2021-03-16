first_player_time = int(input())
second_player_time = int(input())
third_player_time = int(input())

total_time = first_player_time + second_player_time + third_player_time


def total(time):
    hours = time // 60
    minutes = time % 60
    if 0 <= minutes <= 9:
        minutes = f"{minutes:02d}"
    return f"{hours}:{minutes}"


print(total(total_time))
