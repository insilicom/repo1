num = float(input("enter a number: "))
if abs(1000-num) < 100:
    print("within 1000")
elif abs(2000-num) < 100:
    print("within 2000")
else:
    print("not within either number")

