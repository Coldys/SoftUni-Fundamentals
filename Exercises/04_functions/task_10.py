""" 10. Perfect Number """
number = int(input())


def check_num(num):
    divisors = []
    for i in reversed(range(num)):
        if i > 0 and num % i == 0:
            divisors.append(i)

    if sum(divisors) == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(check_num(number))
