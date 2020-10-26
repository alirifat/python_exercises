import os
for dirpath, dirnames, filenames in os.walk('.'):
    print(dirpath)
    print(dirnames)
    print(filenames)
