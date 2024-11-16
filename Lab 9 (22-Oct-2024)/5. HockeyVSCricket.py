universal_set = 40
hockey_players = 21
both_sports = 10

cricket_players = universal_set - (hockey_players - both_sports)

set_hockey = set(range(1, hockey_players + 1))
set_cricket = set(range(1, cricket_players + 1))

cricket_only = set_cricket - set_hockey

print(f"Cricket Only Players = {len(cricket_only)}")
