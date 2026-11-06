arr = [4,3,2,1]

i = 0
j = len(arr) - 1

while i < j:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

    i = i + 1
    j = j - 1

print(arr)