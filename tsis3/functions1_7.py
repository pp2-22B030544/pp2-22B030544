def has33(nums):
    for i in nums :
        if i==3 and i+1==3:
            print("True")
        else :
            print("False")
        

arr =[]
n= int(input())
for i in range (0,n):
    arr.append(int(input()))

otvet = has33(arr)
print(otvet)