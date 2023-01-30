x = input().split()
print("i have" , end='')

for i in range(len(x)) :
    if i < len(x)-1 :
      print(i, ', ', end ='', sep='')
    else:
        print(i, end=' ')

''' print(f' i have {", ".join{x}} in my shopping cart. )
'''

print("in  my shopping cart.")