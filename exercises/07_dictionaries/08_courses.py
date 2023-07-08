courses = {}

while True:
    command = input().split(' : ')

    if command[0] == "end":
        break

    if command[0] in courses:
        courses[command[0]].append(command[1])
    else:
        courses[command[0]] = [command[1]]

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for student in value:
        print(f"-- {student}")
