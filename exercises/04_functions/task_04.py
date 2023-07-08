num = input()


def sum_even_and_odd(number):
    odd = 0
    even = 0
    for i in range(len(number)):
        if int(number[i]) % 2 == 0:
            even += int(number[i])
        else:
            odd += int(number[i])
    return odd, even


sum_of_odd_digits, sum_of_even_digits = sum_even_and_odd(num)

print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
