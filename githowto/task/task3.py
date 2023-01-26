import math
x = int(input())

for i in  range(1, int(math.sqrt(x))+1) :
    print(i*i)


# second method

i=1
while i*i <= x :
    print(i*i)
    i+=1

