user_input = input()


def rounding_number(numbers):
    numbers = numbers.split(' ')
    output = [int(round(float(num))) for num in numbers]
    return output


print(rounding_number(user_input))
