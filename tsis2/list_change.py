thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)
#ans -['apple', 'blackcurrant', 'cherry']


#2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)
# ans - ["apple", "blackcurrant", "watermelon", "orange", "kiwi", "mango" ]


#3
thislist = ["apple", "banana", "cherry"]

thislist[1:2] = ["blackcurrant", "watermelon"]

print(thislist)
#ans - ['apple', 'blackcurrant', 'watermelon', 'cherry']

#4
thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")

print(thislist) 
#ans - ['apple', 'banana', 'watermelon', 'cherry']