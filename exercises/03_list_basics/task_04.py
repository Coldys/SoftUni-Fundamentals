items = input()
items = [int(item) for item in items.split(', ')]
beggars = int(input())
output = []
for i in range(beggars):
    beggar_item = items[i::beggars]
    output.append(sum(beggar_item))

print(output)
