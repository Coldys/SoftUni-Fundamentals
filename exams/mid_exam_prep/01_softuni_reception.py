employees_capability = [int(input()) for x in range(3)]
questions_per_hour = sum(employees_capability)
students = int(input())

employees_break = 4
needed_hours = 0
while students > 0:
    needed_hours += 1
    students -= questions_per_hour
    if needed_hours % employees_break == 0:
        needed_hours += 1

print(f"Time needed: {needed_hours}h.")
