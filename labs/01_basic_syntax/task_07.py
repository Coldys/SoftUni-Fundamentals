num = int(input())
shape = "*"
for i in range(num):
    print(shape)
    shape += "*"

for i in reversed(range(num)):
    print(shape[0:i])
