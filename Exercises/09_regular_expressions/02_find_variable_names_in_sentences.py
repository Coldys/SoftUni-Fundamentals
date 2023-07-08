import re

output = []
user_input = input()

matches = re.findall(r"\b_([0-9-A-Za-z]+)\b", user_input)
# matches = re.findall(r"\b_(\w+)\b", user_input)
output.extend(matches)

print(','.join(output))
