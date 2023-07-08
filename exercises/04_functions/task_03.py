start = input()
end = input()


def get_symbols(a, b):
    output = ""
    for i in range(ord(a) + 1, ord(b)):
        output += chr(i) + ' '
    return output[:-1]


print(get_symbols(start, end))
