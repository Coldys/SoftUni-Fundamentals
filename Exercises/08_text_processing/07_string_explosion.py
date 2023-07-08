text = input()
output = ''
i = 0
magnitude = 0

while True:
    if i >= len(text):
        break

    if magnitude > 0:
        magnitude -= 1

    if text[i] == '>':
        output += '>'
        magnitude += int(text[i + 1])
        i += 1
    elif magnitude == 0 and not text[i].isnumeric():
        output += text[i]

    i += 1


print(output)
