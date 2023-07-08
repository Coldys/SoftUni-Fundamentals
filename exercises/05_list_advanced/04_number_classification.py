user_input = input().split(', ')
positive = [x for x in user_input if int(x) >= 0]
negative = [x for x in user_input if int(x) < 0]
even = [x for x in user_input if int(x) % 2 == 0]
odd = [x for x in user_input if int(x) % 2 != 0]

print(f'Positive: {", ".join(positive)}')
print(f'Negative: {", ".join(negative)}')
print(f'Even: {", ".join(even)}')
print(f'Odd: {", ".join(odd)}')