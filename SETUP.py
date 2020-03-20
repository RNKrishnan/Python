import urllib.request
import urllib.error
from openpyxl import Workbook
from openpyxl.styles import Font
import os
os.chdir('D:\\PROJECT_RENAME')
WB = Workbook()
WS = WB.create_sheet(index=0,title='URL')
WB.save('URL_CHECK.xlsx')

HEADING = ['URL','STATUS']

WS.append(HEADING)
F = Font(name='Arial', size=14, bold = True)
WS['A1'].font=F
WS['B1'].font=F

WB.save('URL_CHECK.xlsx')

URLS = ['https://www.google.com/',
        'https://www.goole.com/',
        'http://www.google.com/',
        'https://dos.python.org/',
        'https://docs.python.org/']

for URL in URLS:
    try:
        U1 = urllib.request.urlopen(URL)
        if U1.code == 200:
            UP= f'{URL},OK'.split(',')
            print(UP)
            WS.append(UP)
            WB.save('URL_CHECK.xlsx')
    except urllib.error.URLError as e:
        ERROR = e.reason
        NURL,ERR,NOTOK= f'{URL},{ERROR},NOT OK'.split(',')
        NOT_URL=[NURL,NOTOK]
        print(NOT_URL)
        WS.append(NOT_URL)
        WB.save('URL_CHECK.xlsx')


    #try:urllib.request.urlopen(URL)
    #except urllib.error.URLError as e:
     #   print(e.reason)
