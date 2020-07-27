import os

#Program will load in 3 files that are not ordered properly
#Program will then automatically rename them so they are ordered properly


#Load example files

#Creates new folder for files
FILE_NAME = 'FilesEx'

if(os.path.exists(FILE_NAME)):
    os.rmdir(FILE_NAME)
    os.mkdir(FILE_NAME)
else:
    os.mkdir(FILE_NAME)

#Makes the new folder the main directory for Python to create files in
os.chdir(os.path.join((os.getcwd()), FILE_NAME))
print(os.getcwd())


#Creates files
open('A3.txt', "x")
open('B1.txt', "x")
open('Z2.txt', "x")


#Sort example files (run after all files loaded)

for file in os.listdir():
    file_name, file_ext = os.path.splitext(file)
    file_num = file_name[len(file_name) - 1]
    os.rename(file, '{} - {}{}'.format(file_num, file_name, file_ext))
    print(file)
