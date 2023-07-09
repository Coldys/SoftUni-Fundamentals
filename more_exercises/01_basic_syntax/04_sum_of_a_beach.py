user_input = input().lower()

total = 0

total += user_input.count('sand')
total += user_input.count('water')
total += user_input.count('fish')
total += user_input.count('sun')

print(total)
