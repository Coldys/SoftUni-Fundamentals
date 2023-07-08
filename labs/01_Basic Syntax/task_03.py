word = input()
output = ""
for i in reversed(range(len(word))):
    output += word[i]

print(output)
