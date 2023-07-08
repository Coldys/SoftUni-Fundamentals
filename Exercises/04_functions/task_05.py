numbers = input().split(' ')
numbers = [int(num) for num in numbers]
print(list(filter(lambda x: (int(x) % 2 == 0), numbers)))
