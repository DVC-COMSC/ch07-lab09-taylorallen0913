names = list(input().split())

min_name = names[0]
max_name = names[0]

for name in names:
    if name < min_name:
        min_name = name
    if name > max_name:
        max_name = name

print(min_name, max_name)