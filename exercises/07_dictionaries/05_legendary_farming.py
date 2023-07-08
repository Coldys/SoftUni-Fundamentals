money = {}
legendary_item = {
    "Shadowmourne": 250,
    "Valanyr": 250,
    "Dragonwrath": 250
}
is_on = True
while is_on:
    user_input = input().split(' ')

    n = len(user_input)
    for i in range(0, n, 2):
        key = user_input[i + 1].lower()
        value = int(user_input[i])

        if key in money:
            money[key] += value
            if key == 'shards' and money[key] >= 250:
                is_on = False
                break
            elif key == 'fragments' and money[key] >= 250:
                is_on = False
                break
            elif key == 'motes' and money[key] >= 250:
                is_on = False
                break
        else:
            money[key] = value
            if key == 'shards' and money[key] >= 250:
                is_on = False
                break
            elif key == 'fragments' and money[key] >= 250:
                is_on = False
                break
            elif key == 'motes' and money[key] >= 250:
                is_on = False
                break

for currency in money:
    if money[currency] >= 250:
        if currency == 'shards':
            legendary_item["Shadowmourne"] = "obtained!"
            money[currency] -= 250
        elif currency == 'fragments':
            legendary_item["Valanyr"] = "obtained!"
            money[currency] -= 250
        elif currency == 'motes':
            legendary_item["Dragonwrath"] = "obtained!"
            money[currency] -= 250

for key, value in legendary_item.items():
    if value == "obtained!":
        print(f'{key} {value}')

if 'shards' in money:
    print(f'shards: {money["shards"]}')
    money.pop('shards')
else:
    print('shards: 0')
if 'fragments' in money:
    print(f'fragments: {money["fragments"]}')
    money.pop('fragments')
else:
    print('fragments: 0')
if 'motes' in money:
    print(f'motes: {money["motes"]}')
    money.pop('motes')
else:
    print('motes: 0')
for key, value in money.items():
    print(f'{key}: {value}')
