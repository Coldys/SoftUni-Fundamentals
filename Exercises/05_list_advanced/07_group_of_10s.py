numbers = input().split(', ')


group = 10
while numbers:
    new_seq = []
    for i in range(len(numbers)):
        current_num = int(numbers[i])
        if current_num <= group:
            new_seq.append(current_num)

    for num in new_seq:
            numbers.remove(str(num))

    print(f"Group of {group}'s: {new_seq}")
    group += 10
