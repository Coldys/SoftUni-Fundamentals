n = int(input())

has_open = None
has_close = None
balanced = True
for _ in range(n):
    user_input = input()
    if user_input == '(':
        if has_open:
            balanced = False
            break
        elif has_open is None:
            has_open = True
            has_close = None
            balanced = False
    elif user_input == ')':
        if has_close or has_open is None:
            balanced = False
            break
        elif has_close is None:
            has_close = True
            has_open = None
            balanced = True

if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
