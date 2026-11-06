arr = [4, 9, 1, 7, 3]

maximum = arr[0]
minimum = arr[0]

for i in arr:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print("Max =", maximum)
print("Min =", minimum)