countries = {x: y for (x, y) in zip(input().split(', '), input().split(', '))}

for country, capital in countries.items():
    print(f'{country} -> {capital}')
