numbers = input()
numbers = [int(x) for x in numbers.split(' ')]
n = int(input())

exclude = numbers.copy()
exclude.sort(reverse=True)
exclude = exclude[len(numbers)-n:]
output = ""

for x in numbers:
    if x not in exclude:
        output += str(x) + ', '


print(output[:-2])
