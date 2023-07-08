n = int(input())
heroes = {}
for _ in range(n):
    name, hit_points, mana_points = input().split(' ')
    if int(hit_points) > 100:
        hit_points = 100

    if int(mana_points) > 200:
        mana_points = 200
    heroes[name] = [int(hit_points), int(mana_points)]


def cast_spell(data, hero: str, mp: int, spell_name: str):
    if data[hero][1] >= mp:
        data[hero][1] -= mp
        print(f"{hero} has successfully cast {spell_name} and now has {data[hero][1]} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell_name}!")
    return data


def take_damaged(data, hero: str, damage: int, attacker: str):
    if (data[hero][0] - damage) > 0:
        data[hero][0] -= damage
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {data[hero][0]} HP left!")
    else:
        del data[hero]
        print(f"{hero} has been killed by {attacker}!")
    return data


def recharge(data, hero: str, amount: int):
    if data[hero][1] + amount > 200:
        recovered = 200 - data[hero][1]
        data[hero][1] = 200
    else:
        recovered = amount
        data[hero][1] += amount

    print(f"{hero} recharged for {recovered} MP!")
    return data


def heal(data, hero: str, amount: int):
    if data[hero][0] + amount > 100:
        recharged = 100 - data[hero][0]
        data[hero][0] = 100
    else:
        recharged = amount
        data[hero][0] += amount

    print(f"{hero} healed for {recharged} HP!")
    return data


while True:
    command = input().split(' - ')

    if command[0] == 'End':
        break

    elif command[0] == 'CastSpell':
        heroes = cast_spell(heroes, command[1], int(command[2]), command[3])

    elif command[0] == 'TakeDamage':
        heroes = take_damaged(heroes, command[1], int(command[2]), command[3])

    elif command[0] == 'Recharge':
        heroes = recharge(heroes, command[1], int(command[2]))

    elif command[0] == 'Heal':
        heroes = heal(heroes, command[1], int(command[2]))

for key in heroes:
    print(key)
    print(f"  HP: {heroes[key][0]}")
    print(f"  MP: {heroes[key][1]}")
