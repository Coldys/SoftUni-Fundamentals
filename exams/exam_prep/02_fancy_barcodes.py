import re

pattern = r'@[#]+([A-Z][A-Za-z0-9]{4,}[A-Z])@[#]+'
n = int(input())


for i in range(n):
    barcodes = input()
    matches = re.findall(pattern, barcodes)

    if len(matches) > 0:
        group = ''
        for ch in matches[0]:
            if ch.isdigit():
                group += ch

        if len(group) == 0:
            group = '00'
        print(f"Product group: {group}")
    else:
        print("Invalid barcode")
