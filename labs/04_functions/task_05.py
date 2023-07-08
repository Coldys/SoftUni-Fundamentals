product = input()
qty = int(input())


def calc_price(item, quantity):
    return {
        'coffee': quantity * 1.50,
        'coke': quantity * 1.40,
        'water': quantity * 1.00,
        'snacks': quantity * 2.00
    }.get(item, "Invalid Product!")


print(f"{calc_price(product, qty):.2f}")
