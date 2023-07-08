text = input()
for i in range(len(text)):
    if text[i] == ':':
        if i + 2 <= len(text):
            print(text[i:i + 2])
