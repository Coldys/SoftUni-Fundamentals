import re

text = input()

patter = r'@([A-Za-z]{3,})@@([A-Za-z]{3,})@|#([A-Za-z]{3,})##([A-Za-z]{3,})#'

matches = re.findall(patter, text)

pairs = 0
mirror_pairs = []
for match in matches:
    if match[0] != '':
        pairs += 1
        if match[0] == match[1][::-1]:
            mirror_pairs.append([match[0], match[1]])
    elif match[2] != '':
        pairs += 1
        if match[2] == match[3][::-1]:
            mirror_pairs.append([match[2], match[3]])

if pairs == 0:
    print("No word pairs found!")
else:
    print(f"{pairs} word pairs found!")


if len(mirror_pairs) > 0:
    output = []
    for pair in mirror_pairs:
        output.append(f'{pair[0]} <=> {pair[1]}')
    print('The mirror words are:')
    print(', '.join(output))
else:
    print('No mirror words!')
