#Slicing
b = "Hello, World!"
print(b[2:5])

#2
b = "Hello, World!"
print(b[:5]) # 5 not included

#3
b = "Hello, World!"
print(b[2:])

#4
b = "Hello, World!"
print(b[-5:-2])

# Upper case
a = "Hello, World!"
print(a.upper())

#lower
a = "Hello, World!"
print(a.lower())

#delete space
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#replace
a = "Hello, World!"
print(a.replace("H", "J"))

#split
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#String format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


#index
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#Escape Character
txt = "We are the so-called \"Vikings\" from the north."
# output : We are the so-called "Vikings" from the north.
