lines = int(input())
tank = 0

for i in range(lines):
    liters = int(input())
    if tank + liters <= 255:
        tank += liters
    elif tank + liters > 255:
        print("Insufficient capacity!")

print(tank)
