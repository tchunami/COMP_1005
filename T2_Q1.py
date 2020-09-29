x = 100

while True:
    if x % 3 == 0:
        print("The number", x, "is divisible by 3.")
    else:
        print("The number", x, "is not divisible by 3.")
    if x == 65:
        break
    x -= 1
