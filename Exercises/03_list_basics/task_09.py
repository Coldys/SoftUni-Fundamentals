items = input().split('|')
budget = float(input())

bought_items = []
current_budget = budget

for i in range(len(items)):
    item = items[i].split('->')
    if float(item[1]) <= current_budget:  # Check if item can be bought
        # Check what type if item and if is not over the max price
        if item[0] == 'Clothes' and float(item[1]) <= 50.0:
            bought_items.append(round(float(item[1]) * 1.4, 2))  # Add item to list with bought items
            current_budget -= float(item[1])  # subtract the price from current budget
        elif item[0] == 'Shoes' and float(item[1]) <= 35.0:
            bought_items.append(round(float(item[1]) * 1.4, 2))  # Add item to list with bought items
            current_budget -= float(item[1])  # subtract the price from current budget
        elif item[0] == 'Accessories' and float(item[1]) <= 20.5:
            bought_items.append(round(float(item[1]) * 1.4, 2))  # Add item to list with bought items
            current_budget -= float(item[1])  # subtract the price from current budget

# Format and print bought items and the budget
print(' '.join([str("{:.2f}".format(x)) for x in bought_items]))
print(f'Profit: {sum(bought_items)+current_budget-budget:.2f}')

# check if we can afford the trip to France
if sum(bought_items) + current_budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
