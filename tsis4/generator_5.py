def number(n):
    while n>-1:
        yield n
        n-=1


n= int(input())
for num in number(n):
    print(num)