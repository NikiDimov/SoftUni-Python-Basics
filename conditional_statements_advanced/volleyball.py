year = input()
p_holidays = int(input())
home_town = int(input())


def volleyball_matches(year, p_holidays, home_town):
    weekends = 48
    total_games = 0
    total_games += home_town
    weekends -= home_town
    total_games += p_holidays * 2 / 3
    total_games += weekends * 3 / 4
    if year == "normal":
        return int(total_games)
    return int(total_games*1.15)


print(volleyball_matches(year, p_holidays, home_town))
