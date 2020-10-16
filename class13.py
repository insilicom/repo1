#marks =int(input('Enter your marks: '))

#if marks >=90:
#    print('Grade A')
#elif marks >= 70:
#    print('Grade B')
#else:
#    print('failed')

names = ["Alice","Bob","Charlie"]
print(names[0])
print(names[1])
print(names[2])

numbers = [1,1,1,1,1]
print(names+numbers)

print("Alice" in names)

names.append('David')
print(names)
print(len(names))

names.insert(1,'Adam')
print(names)

numbers = list(range(10))
print(numbers)

def function1():
    print("call funcetion1 ")
    print(names)
    print("function1 ends")

function1()

for x in range(6):
    print(x)

