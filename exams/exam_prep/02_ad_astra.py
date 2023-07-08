import re
pattern = r'#([A-Za-z\s]+)#(\d{2}\/\d{2}\/\d{2})#(\d+)#|\|([A-Za-z\s]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|'

text = input()

matches = re.findall(pattern, text)
items = []
dates = []
calories = []
for match in matches:
    if match[0] != '':
        items.append(match[0])
        dates.append(match[1])
        calories.append(int(match[2]))
    else:
        items.append(match[3])
        dates.append(match[4])
        calories.append(int(match[5]))

days = sum(calories) // 2000

print(f"You have food to last you for: {days} days!")
for i in range(len(items)):
    print(f"Item: {items[i]}, Best before: {dates[i]}, Nutrition: {calories[i]}")