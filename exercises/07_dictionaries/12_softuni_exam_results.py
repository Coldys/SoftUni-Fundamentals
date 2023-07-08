students = {}
lang = {}

while True:
    command = input().split('-')

    if command[0] == 'exam finished':
        break

    if command[1] == 'banned':
        del students[command[0]]
        continue

    lang[command[1]] = lang.get(command[1], 0) + 1

    if command[0] in students:
        if int(command[2]) > students[command[0]]:
            students[command[0]] = int(command[2])
    else:
        students[command[0]] = int(command[2])

print('Results:')
for key, value in students.items():
    print(f'{key} | {value}')

print('Submissions:')
for key, value in lang.items():
    print(f'{key} - {value}')
