is_on = True

while is_on:
    num = float(input())
    if 1 <= num <= 100:
        print(f"The number {num} is between 1 and 100")
        is_on = False
