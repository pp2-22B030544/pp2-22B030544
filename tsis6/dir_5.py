a = open(r"C:\Users\Жанель\OneDrive\Рабочий стол\tsis6>python dir_5.py").readlines()
f = open("C.txt", "a")
for i in a:
    f.write(i)
f.write("\n")
f.close()
f = open("C.txt").read()
print(f)