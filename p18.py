a = int(input("enter number a: "))
b = int(input("enter number b: "))
c = int(input("enter number c: "))


if a == b and b == c:
    print("Bingo!", 3*(a+b+c))
else:
    print(a+b+c)

