arr = [-1, 2, 0, -3, 5, 0]

pos = 0
neg = 0
zero = 0

for i in arr:
    if i > 0:
        pos = pos + 1
    elif i < 0:
        neg = neg + 1
    else:
        zero = zero + 1

print("Positive =", pos)
print("Negative =", neg)
print("Zero =", zero)