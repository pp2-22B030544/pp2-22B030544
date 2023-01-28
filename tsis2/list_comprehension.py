fruits = ["apple", "banana", "mango", "orange"]

newlist = [x for x in fruits if "a" in x]
print(newlist)

#the syntax
#newlist = [expression for item in iterable if condition == True]

#2
fruits = ["apple", "banana", "mango", "orange"]
newlist = [x for x in fruits if x!="mango"]
print(newlist)

#3 iterable
newlist = [x for x in range(10)]

print(newlist)

#4
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

#5 orangega ayusturady
fruits = ["apple", "banana", "cherry", "banana", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
