arr2 = [100 , "Astana", -10, 1, 10.4, True, 3, 4, 70, 24, -9, "Almaty", "Aktau"]

only_int =[]
only_strin =[]
only_float= []
bools =[]

for i in arr2 :
    if isinstance(i, bool):
        bools.append(i)
    elif isinstance(i, int):
        only_int.append(i)
    elif isinstance(i, str) :
        only_strin.append