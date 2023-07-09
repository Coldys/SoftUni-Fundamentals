key = int(input())
n = int(input())

output = ''

for _ in range(n):
    org_code = ord(input())
    actual_letter = org_code + key
    output += chr(actual_letter)

print(output)
