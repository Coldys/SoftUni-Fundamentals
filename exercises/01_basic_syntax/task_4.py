divisor = int(input())
n = int(input())

for i in reversed(range(1, n + 1)):
    if i % divisor == 0:
        print(i)
        break