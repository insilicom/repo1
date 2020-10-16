def square(x):
    return x**2

print(square(4))

print((lambda x:x**2)(20))

newlist = [10,20,30,40,50]
print(list(map( square, newlist)))

newlist = [1,3,4,5,2,7,11,13,11]

print(list(filter(lambda x: x%2 == 0, newlist)))

def even_num(x):
    for i in range(x):
        if i%2 == 0:
            yield i

print(list(even_num(55)))

