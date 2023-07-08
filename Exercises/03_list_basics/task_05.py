arr = input()
arr = arr.split(' ')
shuffles = int(input())

for i in range(shuffles):
    start = arr[0]
    end = arr[-1]
    middle = int(len(arr)/2)
    first_half = arr[1:middle]
    second_half = arr[middle:-1]
    new_middle = []
    for j in range(len(first_half)):
        new_middle.append(second_half[j])
        new_middle.append(first_half[j])
    arr = [start] + new_middle + [end]

print(arr)
