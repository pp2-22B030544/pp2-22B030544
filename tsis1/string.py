print("Hello")
print('Hello')

#2
a = "Hello"
print(a)

#3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#4 
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#5
a = "Hello, World!"
print(a[1])

#6 for loop
for x in "banana":
  print(x)

#7string length
a = "Hello, World!"
print(len(a))


#8check
txt = "The best things in life are free!"
print("free" in txt)

#9 if
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#10 bool 
txt = "The best things in life are free!"
print("expensive" not in txt)

#11 if not
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")