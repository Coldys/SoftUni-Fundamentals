n = int(input())

for i in range(1, n + 1):
    txt = str(i)
    total_sum = 0
    for j in range(len(txt)):
        total_sum += int(txt[j])

    if total_sum in [5, 7, 11]:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')
