user_input = input().split(', ')

if user_input[-1] == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    wolf_idx = None
    for i in range(len(user_input)):
        if user_input[i] == 'wolf':
            wolf_idx = i
            break

    sheep_idx = len(user_input) - wolf_idx - 1
    print(f"Oi! Sheep number {sheep_idx}! You are about to be eaten by a wolf!")
