usernames = input().split(', ')
good_usernames = []

for username in usernames:
    # check length
    if not 3 <= len(username) <= 16:
        continue

    # check if it has number
    not_valid = False
    for letter in username:
        if not (letter.isalnum() or letter == '_' or letter == '-'):
            not_valid = True
    if not_valid:
        continue

    if ' ' in username:
        continue

    good_usernames.append(username)

for username in good_usernames:
    print(username)
