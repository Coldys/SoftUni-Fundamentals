import re
pattern = r'^>>([A-z]+)<<([0-9\.]+)!(\d+)'
furniture = []
total_cost = 0
while True:

    user_input = input()

    if user_input == 'Purchase':
        break

    match = re.findall(pattern, user_input)

    if len(match) > 0:
        furniture.append(match[0][0])
        price = float(match[0][1])
        qty = int(match[0][2])
        total_cost += price * qty


print('Bought furniture:')

for i in range(len(furniture)):
    print(furniture[i])

print(f'Total money spend: {total_cost:.2f}')
