password = input()


def check_password(string):
    output = []
    if any(not letter.isalnum() for letter in string):
        output.append("Password must consist only of letters and digits")

    if not 6 <= len(string) <= 10:
        output.append("Password must be between 6 and 10 characters")

    if sum(c.isdigit() for c in string) < 2:
        output.append("Password must have at least 2 digits")

    if len(output) == 0:
        return "Password is valid"
    else:
        str_output = ""
        for i in range(len(output)):
            str_output += output[i] + "\n"
        return str_output[:-1]


print(check_password(password))
