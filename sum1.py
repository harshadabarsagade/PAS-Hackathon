n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total = total + 1/i

print(round(total, 4))