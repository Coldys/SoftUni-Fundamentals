is_on = True
coffees = 0

words = ["coding", "dog", "cat", "movie"]
capital_words = ["CODING", "DOG", "CAT", "MOVIE"]
while is_on:
    command = input()

    if command.lower() == "end":
        is_on = False
        break

    if command in words:
        coffees += 1
    elif command in capital_words:
        coffees += 2

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)