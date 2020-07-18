import os

if(os.path.exists("myfile.txt")):
    os.remove("myfile.txt")

f = open("myfile.txt", "x")
f.write("Hello Little Child")
f.close()