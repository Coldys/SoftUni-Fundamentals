iterations = int(input())
output = 0
for i in range(iterations):
    letter = input()
    output += ord(letter)

print(f"The sum equals: {output}")