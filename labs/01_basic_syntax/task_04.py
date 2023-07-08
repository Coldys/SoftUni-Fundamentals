iterations = int(input())
output = ""
for i in range(iterations):
    num = int(input())

    if num % 2 != 0:
        output = f"{num} is odd!"
        break

if output == "":
    output = "All numbers are even."

print(output)
