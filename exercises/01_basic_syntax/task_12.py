quantity = int(input())
days = int(input())

budget = 0
total_spirit = 0
items_to_buy = quantity

for i in range(1, days + 1):
    if i % 11 == 0:
        items_to_buy += 2

    if i % 2 == 0:
        budget += (items_to_buy * 2)
        total_spirit += 5

    if i % 3 == 0:
        budget += (items_to_buy * 8)
        total_spirit += 13

    if i % 5 == 0:
        budget += (items_to_buy * 15)
        total_spirit += 17

        if i % 3 == 0:
            total_spirit += 30

    if i % 10 == 0:
        total_spirit -= 20
        budget += 23

if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")
