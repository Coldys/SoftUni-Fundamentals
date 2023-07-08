user_input = input().split(' ')
output = []
for word in user_input:
    ascii_code = ''
    for i in range(len(word)):
        if word[i].isnumeric():
            ascii_code += word[i]

    new_word = ''
    # reverse last and second letters
    if len(word) - len(ascii_code) >1:
        new_word = word[-1] + word[len(ascii_code) + 1:-1] + word[len(ascii_code)]
    # case when we have less than two letters in a word
    else:
        new_word = word[-1]

    # compile the right word and add it to a list
    new_word = chr(int(ascii_code)) + new_word
    output.append(new_word)

# print the output
print(' '.join(output))
