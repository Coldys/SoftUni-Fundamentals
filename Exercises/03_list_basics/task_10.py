""" 10. * Bread Factory """
energy = 100
coins = 100

user_input = input().split('|')
output = ''

for event in user_input:
    action, points = event.split('-')
    if action == "rest":
        new_energy = energy + int(points)
        if new_energy > 100:
            new_energy = 100
        print(f"You gained {new_energy - energy} energy.")
        energy = new_energy
        print(f"Current energy: {energy}.")
    elif action == 'order':
        if energy - 30 >= 0:
            energy -= 30
            coins += int(points)
            print(f"You earned {points} coins.")
        else:
            new_energy = energy + 50
            if new_energy > 100:
                new_energy = 100
            energy = new_energy
            print("You had to rest!")
    else:
        if coins - int(points) >= 0:
            coins -= int(points)
            print(f"You bought {action}.")
        elif coins - int(points) < 0:
            output = f"Closed! Cannot afford {action}."
            break

if output != '':
    print(output)
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
