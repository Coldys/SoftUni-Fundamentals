string_1 = input()
string_2 = input()
output = ""

for i in range(len(string_1)):
    new_str = string_2[:i+1] + string_1[i+1:]
    if new_str != output and new_str != string_1:
        output = new_str
        print(output)