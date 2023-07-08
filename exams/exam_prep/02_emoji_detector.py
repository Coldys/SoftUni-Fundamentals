import re
text = input()

digits = re.findall(r'\d', text)
digits = [int(x) for x in digits]
cool_threshold = digits[0]
for i in range(1, len(digits)):
    cool_threshold *= digits[i]

emojis = re.findall(r'(\*\*|::)([A-Z][a-z]{2,})\1', text)
cool_emojis = []
for emoji in emojis:
    total_coolness = 0
    for ch in emoji[1]:
        total_coolness += ord(ch)
    if total_coolness >= cool_threshold:
        cool_emojis.append(f'{emoji[0]}{emoji[1]}{emoji[0]}')

print(f'Cool threshold: {cool_threshold}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')
for em in cool_emojis:
    print(em)
