orders = int(input())
total = 0
for i in range(orders):

    price = float(input())
    days = int(input())
    capsules = int(input())

    if price < 0.01 or 100 < price:
        continue
    if days < 1 or 31 < days:
        continue
    if capsules < 1 or 2000 < capsules:
        continue

    order_price = capsules * days * price

    total += order_price
    print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total:.2f}")