ls = input().split(', ')
ls = [int(x) for x in ls]

new_ls = []
ins_idx = 0
for i in range(len(ls)):
    curr = ls[i]
    if ls[i] != 0:
        new_ls.insert(ins_idx, ls[i])
        ins_idx += 1
    else:
        new_ls.append(0)

print(new_ls)
