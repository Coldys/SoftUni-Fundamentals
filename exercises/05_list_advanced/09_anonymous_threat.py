def main():
    user_input = input().split(' ')

    while True:
        command = input()  # get user command

        # Stop case
        if command == '3:1':
            break

        command = command.split(' ')
        # Evoke merge function and passing both parameters from user command
        if command[0] == 'merge':
            user_input = merge(user_input, int(command[1]), int(command[2]))

        # Evoke divide function and passing both parameters from user command
        elif command[0] == 'divide':
            user_input = divide(user_input, int(command[1]), int(command[2]))

    print(' '.join(user_input))  # Print the output


def merge(data, start, end):
    """
    Merge all strings between start and end indexes
    """
    new_str = ''
    if start < 0:  # check starting index
        start = 0

    if end > len(data) - 1:  # check ending index
        end = len(data) - 1

    for i in range(start, end + 1):  # Concatenate all elements as single string
        new_str += data[i]

    if start == 0:
        new_data = [new_str] + data[end+1:]  # Case when starting index is 0
    else:
        new_data = data[:start] + [new_str]  # case when merging elements are not in the begging
        if end != len(data) - 1:
            new_data = new_data + data[end+1:]  # check if there is elements after the merged ones

    return new_data


def divide(data, idx, partitions):
    """
    Split a word on given index on number of partitions
    """

    if partitions > len(data[idx]):  # Check if partition size is bigger than actual word
        step = 1
    else:
        step = len(data[idx]) // partitions  # Calculate number of symbols in each partitions

    word = data.pop(idx)  # Remove and get hold the word that needs to be split

    start = 0
    for parts in range(partitions):
        # Case for last word
        if parts == partitions - 1:
            data.insert(idx, word[start::])  # Insert current partition
            break
        else:
            data.insert(idx, word[start: start + step:])  # Insert current partition

        start += step  # Increment the start index with number of symbols
        idx += 1  # Increment the index

    return data


if __name__ == "__main__":
    main()
