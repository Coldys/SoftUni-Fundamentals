num = int(input())

for i in range(0, num):
    for j in range(0, num):
        for k in range(0,num):
            print(f'{chr(i + 97)}{chr(j + 97)}{chr(k + 97)}')
            