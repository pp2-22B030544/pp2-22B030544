a = [1, 1.2, "mrn", 3.4, 7, "sf"]

is_float = lambda x : isinstance(x, float)
is_str = lambda x : isinstance(x, str)

def count(a, predicate):
    cnt = 0
    for i in a :
        if predicate(i):
            cnt+=1
    return cnt

print(f"float = {}")
    
