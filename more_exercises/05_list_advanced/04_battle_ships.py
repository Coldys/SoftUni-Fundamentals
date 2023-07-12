import re
lines = int(input())

area = []
ships = 0
for _ in range(lines):
    user_input = input().split(' ')
    ships += len(user_input) - user_input.count("0")
    area.append([int(x) for x in user_input])

pattern = r'\b(\d)-(\d)\b'
attacks = re.findall(pattern, input())

for attack in attacks:
    if area[int(attack[0])][int(attack[1])] > 0:
        area[int(attack[0])][int(attack[1])] -= 1

for row in area:
    ships -= len(row) - row.count(0)

print(ships)
