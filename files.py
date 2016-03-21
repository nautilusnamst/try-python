__author__ = 'maxim'

import os

path = "c:/dev/projects/python/firstapp/"

try:
    if os.path.exists(path + "testdir"):  os.removedirs(path + "testdir")
except:
    print("Error while remove")

print(os.listdir(path))

if not os.path.exists(path + "testdir"): os.mkdir(path + "testdir")

print(os.listdir(path))

os.makedirs(path + "dir1/dir2/dir3", exist_ok=True)

print(os.listdir(path))

# write to file

file = open(path + "testdir/hello.txt", "w")
file.write("Hello, pizza!")
file.close()