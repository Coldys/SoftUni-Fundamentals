import re

output = []
while True:
    user_input = input()

    if not user_input:
        break

    matches = re.findall(r"\d+", user_input)
    output.extend(matches)

print(' '.join(output))
