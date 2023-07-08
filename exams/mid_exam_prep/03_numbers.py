numbers = [int(x) for x in input().split(' ')]

avg_number = sum(numbers) / len(numbers)

above_agv = sorted([x for x in numbers if x > avg_number])

if not above_agv:
    print('No')
else:
    print(*[above_agv.pop() for i in range(5) if above_agv])
