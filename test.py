##for x in range(1,11):
##    print(x)
##for x in ['apple','banana','orange']:
##    print(x)
#
##ct = 0
##while(ct < 11):
##    print(ct)
##    ct=ct+1
#
#
##a = 1
##b = 1
##for x in range(1,11):
##    c=a+b
##    a=b
##    b=c
##    print( c)
#
#file = open("filetest.py","w")
#file.write("This is the content write to file\n")
#file.close()
#file = open("filetest.py","a")
#file.write("2nd line\n")
#file.close()
#file = open("filetest.py","r")
#line = file.read()
#print(line)
#file.close()

file1 = open("demo.txt",'w')
file1.write("Some random data.")
file1.close()

file2 =  open("demo.txt",'r')
myfile = file2.read()
print(myfile)
file2.close()

file3 = open("demo.txt",'a')
file3.write("\nAdd new data")
file3.close()

