user_input = input()

digits = []
letter = ''

for ch in user_input:
    if ch.isnumeric():
        digits.append(int(ch))
    else:
        letter += ch

take_digit = []
skip_digits = []

for i in range(len(digits)):
    if i % 2 == 0:
        take_digit.append(digits[i])
    else:
        skip_digits.append(digits[i])

result = ''

for i in range(len(take_digit)):
    result += letter[:take_digit[i]]
    letter = letter[take_digit[i]:]
    letter = letter[skip_digits[i]:]

print(result)
