def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("divided by 0")
        return 

x = float(input("1st number: "))
y = float(input("2nd number: "))

res = div(x,y)
print(res)


