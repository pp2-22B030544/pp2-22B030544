def solve(numheads, numlegs):
    No = "Error"
    for chicken in range (numheads +1):
        rabbits = numheads - chicken
        if 4*rabbits + 2 *chicken == numlegs:
            return rabbits , chicken
    return No 


numheads = 35
numlegs = 94 
rabchick = solve(numheads , numlegs)
# 23 chicken 12 rabbit