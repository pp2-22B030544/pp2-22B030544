def square_up(n) :
    for i in range(1, n+1):
        yield i**2


for square in square_up(6) :
    print(square)