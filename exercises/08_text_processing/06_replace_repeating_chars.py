text = input()
output = ''
current_letter = ''
for i in range(len(text)):
    if text[i] != current_letter:
        current_letter = text[i]
        output += current_letter

print(output)
