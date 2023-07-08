str = input()
num = input()


def get_number_or_string(string, number):
    if string == "int":
        return int(number) * 2
    elif string == "real":
        return f"{float(number) * 1.5:.2f}"
    elif string == "string":
        return f"${number}$"


print(get_number_or_string(str, num))