budget = int(input())
command = input()

while command != "End":
    spending = int(command)
    budget -= spending
    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")
