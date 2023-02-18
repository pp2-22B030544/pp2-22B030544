print(10 > 9) # true
print(10 == 9)  #false
print(10 < 9)   # false


a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#
print(bool("Hello"))
print(bool(15))

#
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# variables false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


#function
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#instance
x ="Zhanel"
print(isinstance(x, str))  #true
# comm