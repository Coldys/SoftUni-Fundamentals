user_input = input().split(', ')

for i in range(len(user_input)):
    print(user_input[i] == user_input[i][::-1])
