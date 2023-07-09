text = input()
indexes = []

for i in range(len(text)):
    points = ord(text[i])
    if 64 < ord(text[i]) < 91:
        indexes.append(i)

print(indexes)
