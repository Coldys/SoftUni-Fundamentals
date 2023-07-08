digits = [int(x) for x in input()]

digits = reversed(sorted(digits))

output = ''
for digit in digits:
    output += str(digit)

print(output)
