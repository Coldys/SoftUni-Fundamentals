user_input = input()
num_array = [int(x) for x in user_input.split(' ')]

print(f"The minimum number is {min(num_array)}")
print(f"The maximum number is {max(num_array)}")
print(f"The sum number is: {sum(num_array)}")
