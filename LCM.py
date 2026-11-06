a = int(input("Enter a:"))
b = int(input("Enter b:"))

lcm = a

while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm = lcm + a

print(lcm)