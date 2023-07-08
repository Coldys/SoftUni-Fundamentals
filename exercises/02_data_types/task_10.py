lost_fights = int(input())
helmet_cost = float(input())
sword_cost = float(input())
shield_cost = float(input())
armor_cost = float(input())

helmets = 0
swords = 0
shields = 0
armors = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        helmets += 1
    if i % 3 == 0:
        swords += 1
        if i % 2 == 0:
            shields += 1
            if shields % 2 == 0:
                armors += 1


cost = (helmet_cost * helmets) + (sword_cost * swords) + (shield_cost * shields) + (armors * armor_cost)

print(f"Gladiator expenses: {cost:.2f} aureus")
