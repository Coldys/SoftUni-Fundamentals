user_input = input().split('.')
user_input = [int(x) for x in user_input]

if user_input[len(user_input) - 1] < 9:
    user_input[len(user_input) - 1] += 1
else:
    user_input[len(user_input) - 1] = 0
    user_input[len(user_input) - 2] += 1
    if user_input[len(user_input) - 2] > 9:
        user_input[len(user_input) - 2] = 0
        user_input[len(user_input) - 3] += 1

print(f'{user_input[0]}.{user_input[1]}.{user_input[2]}')
