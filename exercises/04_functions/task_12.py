num_1 = int(input())
num_2 = int(input())


def factorial(num):
    output = 1
    for i in range(1, num+1):
        output *= i

    return output


factorial_1 = factorial(num_1)
factorial_2 = factorial(num_2)

print(f"{factorial_1/factorial_2:.2f}")
