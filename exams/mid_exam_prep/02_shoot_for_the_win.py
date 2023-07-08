def swap(arr, idx_1: int, idx_2: int):
    if idx_1 in range(len(arr)) and idx_2 in range(len(arr)):
        arr[idx_1], arr[idx_2] = arr[idx_2], arr[idx_1]
    return arr


def multiply(arr, idx_1: int, idx_2: int):
    if idx_1 in range(len(arr)) and idx_2 in range(len(arr)):
        arr[idx_1] *= arr[idx_2]
    return arr


def decrease(arr):
    for i in range(len(arr)):
        arr[i] -= 1
    return arr


initial_list = [int(x) for x in input().split(' ')]

while True:
    command = input()

    if command == 'end':
        break

    command = command.split(' ')

    if command[0] == 'swap':
        initial_list = swap(initial_list, int(command[1]), int(command[2]))
    elif command[0] == 'multiply':
        initial_list = multiply(initial_list, int(command[1]), int(command[2]))
    elif command[0] == 'decrease':
        initial_list = decrease(initial_list)

initial_list = [str(x) for x in initial_list]
print(', '.join(initial_list))
