num = int(input())


def get_bar(number):
    number = int(number / 10)
    if number == 10:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        str_output = ("%" * int(number)) + ("." * (10 - int(number)))
        output = f"{number * 10}% [{str_output}]\nStill loading..."
        return output


print(get_bar(num))
