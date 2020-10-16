#n1 = input('Enter a list of numbers')
n1 = "1,2,3,4,5,6"
n2 = (1,2,3,4,5)

list1 = n1.split(',')
print("n2 type is ", type(n2))

print(list1,type(list1))

tuple1 = tuple(list1)
print(type(tuple1))
