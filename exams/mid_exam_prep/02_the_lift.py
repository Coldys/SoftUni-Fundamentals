people = int(input())
wagons = [int(x) for x in input().split(' ')]

for i in range(len(wagons)):

    can_fit = 4 - wagons[i]

    if can_fit > people:
        can_fit = people

    wagons[i] += can_fit
    people -= can_fit

people_in = sum(wagons)
wagons = [str(x) for x in wagons]

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(f"{' '.join(wagons)}")
elif people_in == len(wagons) * 4:
    print(f"{' '.join(wagons)}")
else:
    print("The lift has empty spots!")
    print(f"{' '.join(wagons)}")
