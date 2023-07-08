user_input = input().split()

output = 0

for text in user_input:
    first_letter = text[0]
    number = int(text[1:-1])
    last_letter = text[-1]
    if first_letter.isupper():
        output += number / (ord(first_letter) - 64)
    elif first_letter.islower():
        output += number * (ord(first_letter) - 96)
    if last_letter.isupper():
        output -= (ord(last_letter) - 64)
    elif last_letter.islower():
        output += (ord(last_letter) - 96)

print(f'{output:.2f}')
