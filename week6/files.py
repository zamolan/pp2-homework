import os

path = "c:\KBTU\pp2"

#1
directories = []
files = []
all_items = os.listdir(path)
for item in all_items:
    if os.path.isdir(os.path.join(path, item)):
        directories.append(item)
    else:
        files.append(item)
print(directories, files, all_items) 

#2
exists = os.path.exists(path)
readable = os.access(path, os.R_OK)
writable = os.access(path, os.W_OK)
executable = os.access(path, os.X_OK)
print(exists, readable, writable, executable) 

#3
if exists:
    print('Path exists:', path)
    filename = os.path.basename(path)
    print('Filename:', filename)
    directory = os.path.dirname(path)
    print('Directory:', directory)
else:
    print("Path does not exist.") 

#4
f = open("demofile.txt", "r")
lines = f.readlines()
print('Count of lines:', len(lines))
f.close() 

#5
f = open("demofile.txt", "a")
l = ["apple", "banana", "cherry"]
for i in l:
    f.write(i + '\n')
f.close()
f = open("demofile.txt", "r")
print(f.read())
f.close() 

#6
for i in range(26):
    filename = chr(65 + i) + ".txt"
    f = open(filename, "x")
    f.close()

#7
source_file = "source.txt"
destination_file = "destination.txt"
with open(source_file, "r") as src, open(destination_file, "w") as dst:
    for line in src:
        dst.write(line)

#8
for i in range(26):
    filename = chr(65 + i) + ".txt"
    if os.path.exists(filename):
        if os.access(filename, os.W_OK):
            os.remove(filename)
        else:
            print("No access")
    else:
        print("Not exist")