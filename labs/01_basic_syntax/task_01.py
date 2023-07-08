number = float(input())
output = ""

if number == 0:
    output = "zero"

if number > 0:
    output += "positive"
elif number < 0:
    output += "negative"

if 0 < abs(number) < 1:
    output = "small " + output
elif abs(number) > 1000000:
    output = "large " + output

print(output)