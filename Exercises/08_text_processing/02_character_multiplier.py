str_1, str_2 = input().split(' ')
total_sum = 0
for i in range(max(len(str_1), len(str_2))):
    if i in range(len(str_1)) and i in range(len(str_2)):
        total_sum += ord(str_1[i]) * ord(str_2[i])
    elif i in range(len(str_1)) and i not in range(len(str_2)):
        total_sum += ord(str_1[i])
    elif i not in range(len(str_1)) and i in range(len(str_2)):
        total_sum += ord(str_2[i])

print(total_sum)
