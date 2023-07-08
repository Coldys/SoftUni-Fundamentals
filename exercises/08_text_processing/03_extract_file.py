file_path = input()
name_end = None
file_name = None
file_type = None
for i in range(len(file_path) - 1, 0, -1):
    if file_path[i] == '.':
        name_end = i
        file_type = file_path[i + 1:]
    elif file_path[i] == '\\':
        file_name = file_path[i + 1:name_end]
        break

print(f'File name: {file_name}')
print(f'File extension: {file_type}')
