def solve(action, a, b):
    return {
        "multiply": a * b,
        "divide": int(a / b),
        "add": a + b,
        "subtract": a - b
    }.get(action, "Invalid Operator!")


operator = input()
num_1 = int(input())
num_2 = int(input())

print(solve(operator, num_1, num_2))
