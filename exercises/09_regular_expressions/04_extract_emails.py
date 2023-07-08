import re

pattern = r'\s(([a-z]+[a-z\-\.\_]+)@([a-z\-]+)(\.[a-z]+)+)\b'
output = []

user_input = input()

match = re.findall(pattern, user_input)

for email in match:
    print(email[0])
