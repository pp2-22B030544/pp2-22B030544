import os

path = r"C:\Users\Жанель\OneDrive\Рабочий стол\tsis6"


dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
print("Directories:")
print(dirs)

files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
print("Files:")
print(files)


dirs_and_files = os.listdir(path)
print("Directories and files:")
print(dirs_and_files)
