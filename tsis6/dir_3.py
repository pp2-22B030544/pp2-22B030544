import os
path = r'C:\\Users\\Жанель\\OneDrive\\Рабочий стол\\tsis6'
if os.path.exists(path):
    fileName = os.path.basename(path)
    path_to_file = os.path.dirname(path)
    print(fileName)
    print(path_to_file)
else:
    print("The path does not exist")
    
