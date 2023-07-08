def main():
    schedule = input().split(', ')

    while True:
        command = input()

        if command == 'course start':
            break

        command = command.split(':')
        if command[0] == 'Add':
            schedule = add_course(schedule, command[1])
        elif command[0] == 'Insert' and len(command) == 3:
            schedule = insert_course(schedule, command[1], int(command[2]))
        elif command[0] == 'Remove':
            schedule = remove_course(schedule, command[1])
        elif command[0] == 'Swap':
            schedule = swap_courses(schedule, command[1], command[2])
        elif command[0] == 'Exercise':
            schedule = add_exercise(schedule, command[1])

    if len(schedule) > 0:
        for i in range(len(schedule)):
            print(f'{i + 1}.{schedule[i]}')


def add_course(data, name):
    """
    Append  the new course on the end of the list
    """
    if name not in data:
        data.append(name)

    return data


def insert_course(data, name, idx):
    """
    Insert a lesson if not already exists in the course user_data
    """
    if idx < 0:
        idx = 0

    if idx > len(data):
        idx = len(data)

    if name not in data:
        data.insert(idx, name)

    return data


def remove_course(data, name):
    """
    Remove given lesson name if present in the user_data
    """
    if name in data:
        idx = data.index(name)
        if idx + 1 in range(len(data)):
            if 'Exercise' in data[idx + 1]:
                data.pop(idx + 1)
        data.pop(idx)
    return data


def swap_courses(data, name_1, name_2):
    """
    swap position on given two indexes
    """
    if name_1 in data and name_2 in data:
        idx_1 = data.index(name_1)
        idx_2 = data.index(name_2)
        first_exercise = False
        second_exercise = False

        if idx_1 + 1 in range(len(data)):
            first_exercise = 'Exercise' in data[idx_1 + 1]
        if idx_2 + 1 in range(len(data)):
            second_exercise = 'Exercise' in data[idx_2 + 1]

        data[idx_1], data[idx_2] = data[idx_2], data[idx_1]

        if first_exercise and second_exercise:
            data[idx_1 + 1], data[idx_2 + 1] = data[idx_2 + 1], data[idx_1 + 1]
        elif not first_exercise and second_exercise:
            data.insert(idx_1 + 1, data.pop(idx_2 + 1))
        elif first_exercise and not second_exercise:
            data.insert(idx_2 + 1, data.pop(idx_1 + 1))

    return data


def add_exercise(data, lesson_name):
    """
    Add exercise right after given lesson name
    """
    if lesson_name in data and f'{lesson_name}-Exercise' not in data:
        idx = data.index(lesson_name) + 1
        data.insert(idx, f'{lesson_name}-Exercise')
    elif lesson_name not in data:
        data.append(lesson_name)
        data.append(f'{lesson_name}-Exercise')

    return data


if __name__ == "__main__":
    main()
