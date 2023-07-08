energy = int(input())
count = 0

while True:
    command = input()

    if command == "End of battle":
        print(f"Won battles: {count}. Energy left: {energy}")
        break

    needed_energy = int(command)
    if needed_energy <= energy:
        energy -= needed_energy
        count += 1
    else:
        print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
        break

    if count % 3 == 0:
        energy += count
