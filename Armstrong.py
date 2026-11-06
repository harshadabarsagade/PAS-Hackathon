n = int(input("Enter number:"))
temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit * digit * digit
    n = n // 10

if temp == sum:
    print("True")
else:
    print("False")