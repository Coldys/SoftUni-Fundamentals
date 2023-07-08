def letter_counter():
    user_input = input()
    letters_counter = {}
    for letter in user_input:
        if letter != ' ':
            letters_counter[letter] = letters_counter.get(letter, 0) + 1

    for key, value in letters_counter.items():
        print(f'{key} -> {value}')


letter_counter()
