n = int(input())
free_chairs = 0
output = ''
for i in range(n):
    room_data = input().split(' ')
    if len(room_data[0]) >= int(room_data[1]):
        free_chairs += len(room_data[0]) - int(room_data[1])
    else:
        output += f'{int(room_data[1]) - len(room_data[0])} more chairs needed in room {i + 1}\n'

if output == '':
    print(f'Game On, {free_chairs} free chairs left')
else:
    print(output[:-1])
