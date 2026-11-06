n = int(input("Enter number:"))
last = n % 10

while n >= 10:
    n = n // 10

print("First =", n)
print("Last =", last)