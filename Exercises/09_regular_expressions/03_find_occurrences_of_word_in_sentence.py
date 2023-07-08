import re
text = input()
word = input()


matches = re.findall(r'\b'+word+r'\b', text, re.IGNORECASE)

print(len(matches))
