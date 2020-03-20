import os
from datetime import datetime,date
import glob
import subprocess

import smtplib


#mail = smtplib.SMTP('smtp.gmail.com',587)

#content ='HI THIS NAVANEE'

#mail.ehlo() 
#mail.starttls()
#mail.login('Mailid','pass')
#mail.sendmail('From','TO',content)
#mail.close()



subprocess.call(r'net use I: "\\Muthupandiv-pc\d" /p:no',shell=True)


os.chdir(r'I:\\')
PATH = os.getcwd()

DATE = datetime.now().strftime('%Y%m%d')
FILE_DATE = f'*{DATE}*'
print(FILE_DATE)

FILE_NAME = glob.glob(FILE_DATE)

print(FILE_NAME)


for F in FILE_NAME:
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
