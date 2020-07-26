import os

#Load example files

FILE_NAME = 'FilesEx'

if(os.path.exists(FILE_NAME)):
    os.rmdir(FILE_NAME)
    os.mkdir(FILE_NAME)
else:
    os.mkdir(FILE_NAME)
os.chdir(os.path.join((os.getcwd()), FILE_NAME))
print(os.getcwd())

"""
#If files exist delete them
open('A3.txt', "x")
open('B1.txt', "x")
open('Z2.txt', "x")
"""

"""
#Sort example files (run after all files loaded)

for file in os.listdir():
    file_name, file_ext = os.path.splitext(file)
    file_num = file_name[len(file_name) - 1]
    os.rename(file, '{} - {}{}'.format(file_num, file_name, file_ext))
    print(file)
"""