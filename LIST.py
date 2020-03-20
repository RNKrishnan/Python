import os
from datetime import datetime
import glob
import math

os.chdir(r'D:\PROJECT_RENAME')
print(os.getcwd())

FILE = glob.glob('*2020*')
i=0
LIS=[]
for F in FILE:
    if os.path.isfile(F):
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(F)
        IST = datetime.fromtimestamp(mtime)
        BST = datetime.utcfromtimestamp(mtime)
        RESIZE = round(int(size) / 1024)
        FILE_SIZE = f'{RESIZE}KB'
        SRT = str(datetime.strftime(BST,'%Y%m%d %H:%M'))
        F_DETAILS= f'{F},{FILE_SIZE},{SRT}'
        #print()
        
        LIS.append(F_DETAILS)
        
                 #print(LIS)
    else:
        print('DIR')
print(LIS)


input("Press enter to exit ;)")
