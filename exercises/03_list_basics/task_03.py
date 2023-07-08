cards = input()
cards = cards.split(' ')

team_A = [True] * 11
team_B = [True] * 11

for i in range(len(cards)):
    player = cards[i].split('-')
    if player[0] == 'A':
        idx = int(player[1]) - 1
        team_A[idx] = False
    else:
        idx = int(player[1]) - 1
        team_B[idx] = False

    if team_A.count(True) < 7 or team_B.count(True) < 7:
        break

print(f"Team A - {team_A.count(True)}; Team B - {team_B.count(True)}")
if team_A.count(True) < 7 or team_B.count(True) < 7:
    print("Game was terminated")
    