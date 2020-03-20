import urllib.request
import urllib.error

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
    except urllib.error.URLError as e:
        print(URL)
        print(e.reason)

        #NURL,ERR,NOTOK= f'{URL},{ERR},NOT OK'.split(',')
        #NOT_URL=[NURL,NOTOK]
