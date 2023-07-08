import re
pattern = r'=([A-Z][A-Za-z]{2,})=|/([A-Z][A-Za-z]{2,})/'

user_input = input()

all_destinations = []
matches = re.findall(pattern, user_input)
travel_points = 0

for match in matches:
    if match[0] != '':
        all_destinations.append(match[0])
        travel_points += len(match[0])
    if match[1] != '':
        all_destinations.append(match[1])
        travel_points += len(match[1])

print(f'Destinations: {", ".join(all_destinations)}')
print(f'Travel Points: {travel_points}')
