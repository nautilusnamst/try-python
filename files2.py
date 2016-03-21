__author__ = 'maxim'

import os
import shutil

path = "c:/dev/projects/python/firstapp/"

#os.removedirs(path + "testdir2")
#os.rmdir(path + "testdir2")
#os.remove(path + "testdir2")
shutil.rmtree(path + "testdir", True)

print(os.listdir(path))