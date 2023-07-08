start = int(input())
end  = int(input()) + 1
output = ""
for i in range(start, end):
    output += chr(i) + " "

print(output[:-1])
