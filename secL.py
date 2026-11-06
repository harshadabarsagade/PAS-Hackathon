arr = [12, 35, 1, 10, 34, 1]

first = 0
second = 0

for i in arr:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i

print("Second largest =", second)