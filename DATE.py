import os
from datetime import datetime
import glob
import math

os.chdir(r'D:\PROJECT_RENAME')
print(os.getcwd())

FILE = glob.glob('NAVA2020*')

for F in FILE:
    if os.path.isfile(F):
        print('FILE')
        (mode,ino,dev,nlink,uid,gid,size,atime,mtime,ctime) = os.stat(F)
        IST = datetime.fromtimestamp(mtime)
        print(IST)
        BST = datetime.utcfromtimestamp(mtime)
        print(BST)
        if size == 0:
            EMPTY = 'FILE SIZE ZERO PLEASE VALIDATE'
            print(EMPTY)
        else:
            print(size)
            RESIZE = round(int(size)/1024)
        
            
            FILE_SIZE = f'FILE SIZE IS: {RESIZE}KB'
            print(FILE_SIZE)
    else:
        print('DIR')

input("Press enter to exit ;)")

