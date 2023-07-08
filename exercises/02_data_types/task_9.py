snowballs = int(input())

best_points = 0
best_weight = None
best_time = None
best_quality = None

for i in range(snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    points = (snowball_weight / snowball_time) ** snowball_quality

    if points > best_points:
        best_points = points
        best_weight = snowball_weight
        best_time = snowball_time
        best_quality = snowball_quality

print(f"{best_weight} : {best_time} = {int(best_points)} ({best_quality})")
