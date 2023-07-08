user_data = input().split('#')
water = int(input())
effort = 0
total_fire = 0
cells = []
for i in range(len(user_data)):
    cell_data = user_data[i].split(' = ')
    if cell_data[0] == 'High' and 81 <= int(cell_data[1]) <= 125:
        cell_value = int(cell_data[1])
        if water >= cell_value:
            water -= cell_value
            effort += cell_value * .25
            total_fire += cell_value
            cells.append(cell_value)
    elif cell_data[0] == 'Medium' and 51 <= int(cell_data[1]) <= 80:
        cell_value = int(cell_data[1])
        if water >= cell_value:
            water -= cell_value
            effort += cell_value * .25
            total_fire += cell_value
            cells.append(cell_value)
    elif cell_data[0] == 'Low' and 1 <= int(cell_data[1]) <= 50:
        cell_value = int(cell_data[1])
        if water >= cell_value:
            water -= cell_value
            effort += cell_value * .25
            total_fire += cell_value
            cells.append(cell_value)

print('Cells:')
for cell in cells:
    print(f' - {cell}')
print(f'Effort: {effort:.2f}')
print(f"Total Fire: {total_fire}")
