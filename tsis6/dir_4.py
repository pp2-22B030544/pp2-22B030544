file_name = input()
with open(file_name, 'r') as f:
    contents = f.read()
    num_lines = contents.count('\n') + 1
    print(f"The number of lines in {file_name} is: {num_lines}")