import os

os.chdir(b'C:\Users\slice\OneDrive\Documents\Python\Files')

for file in os.listdir():
    file_name, file_ext = os.path.splitext(file)
    file_num = file_name[len(file_name) - 1]
    os.rename(file, '{} - {}{}'.format(file_num, file_name, file_ext))
    print(file)