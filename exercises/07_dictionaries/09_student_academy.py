n = int(input())
students = {}
for _ in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

for key, value in students.items():
    avg_grade = sum(value) / len(value)
    if avg_grade >= 4.5:
        print(f"{key} -> {avg_grade:.2f}")
