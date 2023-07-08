budget = float(input())
flour_price = float(input())
egg_price = flour_price * .75
milk_price = flour_price * 1.25

recipe_cost = egg_price + flour_price + (0.250 * milk_price)
colored_eggs = 0
number_of_loaves = 0

while recipe_cost < budget:
    number_of_loaves += 1
    budget -= recipe_cost
    colored_eggs += 3

    if number_of_loaves % 3 == 0:
        colored_eggs -= number_of_loaves - 2

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
