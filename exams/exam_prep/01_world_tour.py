destinations = input()


def add_stop(data, idx, destination):
    if idx in range(len(data)):
        data = data[:idx] + destination + data[idx:]
    return data


def remove_stop(data, start_idx, end_idx):
    if start_idx in range(len(data)) and end_idx in range(len(data)):
        data = data[:start_idx] + data[end_idx + 1:]
    return data


def switch(data, old_str, new_str):
    return data.replace(old_str, new_str)


while True:
    command = input().split(':')
    if command[0] == 'Travel':
        break
    elif command[0] == 'Add Stop':
        destinations = add_stop(destinations, int(command[1]), command[2])
    elif command[0] == 'Remove Stop':
        destinations = remove_stop(destinations, int(command[1]), int(command[2]))
    elif command[0] == 'Switch':
        destinations = switch(destinations, command[1], command[2])

    print(destinations)

print(f"Ready for world tour! Planned stops: {destinations}")
