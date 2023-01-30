thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# clychainui element
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# clear
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset) # ans-set()

# del
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)