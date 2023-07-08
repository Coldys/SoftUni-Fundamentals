text = input()
used_symbols = []
output = ''
curr_text = ''
skip_next = False

for idx, letter in enumerate(text):
    if skip_next:
        skip_next = False
        continue

    if not letter.isnumeric() and letter.upper() not in used_symbols:
        used_symbols.append(letter.upper())

    if not letter.isnumeric():
        curr_text += letter.upper()

    else:
        number = letter
        if idx + 1 <= len(text) - 1 and text[idx + 1].isnumeric():
            number += text[idx + 1]
            skip_next = True
        output += curr_text * int(number)
        curr_text = ''
        number = ''

print(f'Unique symbols used: {len(used_symbols)}')
print(output)
