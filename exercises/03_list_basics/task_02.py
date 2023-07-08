factor = int(input())
count = int(input())

output = []
new_factor = factor
for i in range(count):
    output.append(new_factor)
    new_factor += factor

print(output)
