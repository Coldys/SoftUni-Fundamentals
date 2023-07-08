def check_half(half, sym):
    current_count = 0
    count = 0

    for ch in half:
        if ch == sym:
            current_count += 1
        else:
            count = max(count, current_count)
            current_count = 0

    return max(count, current_count)


tickets = [x.strip() for x in input().split(', ')]

symbols = ['@', '#', '$', '^']
for ticket in tickets:

    if len(ticket) != 20:
        print('invalid ticket')
        continue

    first_half = ticket[:10]
    second_half = ticket[10:]

    current_best = 0
    win_symbol = ''
    for s in symbols:
        result_1 = check_half(first_half, s)
        result_2 = check_half(second_half, s)
        curr = min(result_1, result_2)

        if curr > current_best:
            current_best = curr
            win_symbol = s

    if current_best >= 6:
        if current_best < 10:
            print(f'ticket "{ticket}" - {current_best}{win_symbol}')
        else:
            print(f'ticket "{ticket}" - {current_best}{win_symbol} Jackpot!')
    else:
        print(f'ticket "{ticket}" - no match')
