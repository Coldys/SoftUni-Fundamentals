def string_multiplication(string, n):
    output = string * n
    # print(output)
    return output


user_string = input()
repetitions = int(input())

print(string_multiplication(user_string, repetitions))
