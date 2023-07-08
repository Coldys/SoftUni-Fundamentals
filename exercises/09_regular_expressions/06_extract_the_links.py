import re
pattern = r'\b(www.([A-Za-z0-9\-]+)(\.[A-Za-z]+)+)\b'

while True:
    user_input = input()
    if not user_input:
        break

    match = re.findall(pattern, user_input)

    if len(match) > 0:
        print(match[0][0])
