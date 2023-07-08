n = int(input())

for i in range(n):
    str_input = input()
    if "," in str_input or "_" in str_input or "." in str_input:
        print(f"{str_input} is not pure!")
    else:
        print(f"{str_input} is pure.")