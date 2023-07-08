text = input()
output = ''

for i in range(len(text)):
    output += chr(ord(text[i]) + 3)

print(output)
