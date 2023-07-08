start_year = input()
year = int(start_year)


def check_is_distinct(yr: str):
    is_dist = True
    for i in range(len(yr)):
        if yr.count(yr[i]) > 1:
            is_dist = False
            break

    return is_dist


while True:
    year += 1
    if check_is_distinct(str(year)):
        print(year)
        break
