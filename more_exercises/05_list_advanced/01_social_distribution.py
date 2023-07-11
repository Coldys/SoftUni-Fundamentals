population = [int(x) for x in input().split(', ')]
min_wealth = int(input())

for i in range(len(population)):
    if population[i] < min_wealth:
        max_wealth = population.index(max(population))
        need_wealth = min_wealth - population[i]
        if population[max_wealth] - need_wealth >= min_wealth:
            population[max_wealth] -= need_wealth
            population[i] += need_wealth

is_equal = True
for person in population:
    if person < min_wealth:
        is_equal = False
        break

if is_equal:
    print(population)
else:
    print('No equal distribution possible')
