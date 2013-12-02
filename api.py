import json
import urllib2
import unicodedata

def isMove(string):
    num = False
    alpha = False
    other = False
    other1 = False
    for x in string:
        if x.isdigit():
            num = True
        if x.isalpha():
            alpha = True
        if x <= '-' or (x <= '@' and x >= ':'):
            other = True
    return string.find('.') and num and alpha and not other

#finds all the algebraic notation in the article, returns a list
def findNotation(link):
    #makes the list compatible with mediawiki api
    path = link[link.find("/wiki/")+6:]
    page = urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=query&prop=revisions&format=json&rvprop=content&rvlimit=1&titles=" + path)
    #gets the article out of the page returned by mediawiki
    dict = json.load(page)
    query = dict.keys()[1]
    pages = dict[query]["pages"]
    text = pages.keys()[0]
    c = pages[text]["revisions"][0]["*"]
    f = c.encode('utf-8','ignore')
    d = f.__len__()
    e = f.find('1.')   
    l = f[e:]
    #finds the algebraic notation
    ret = ""
    x = 1
    while (x < 100):
        a = l.find(str(x)+'.')
        b = 1
        if a == -1 or l[a-1] > 'a' and l[a-1] < 'z':
            x = x + 1
        else:
            ret = ret + ' ' + l[a]
            temp = a
            a = a + 1
            while b != 0:
                if (l[a] > '9' and  l[a] < 'x') or l[a] > 'x' or (l[a] < '0' and l[a] > '.') or (l[a] < '.' and l[a] > ' ') or l[a] < ' ':
                    if (l[a+1] > '9' and l[a+1] < 'x') or l[a+1] > 'x' or (l[a+1] < '0' and l[a+1] > '.') or (l[a+1] < '.' and l[a+1] > ' ') or l[a+1] < ' ':
                        if (l[a+2] > '9' and l[a+2] < 'x') or l[a+2] > 'x' or (l[a+2] < '0' and l[a+2] > '.') or (l[a+2] < '.' and l[a+2] > ' ') or l[a+2] < ' ':
                            if (l[a+3] > '9' and l[a+3] < 'x') or l[a+3] > 'x' or (l[a+3] < '0' and l[a+3] > '.') or (l[a+3] < '.' and l[a+3] > ' ') or l[a+3] < ' ':
                                b = 0
                if l[a] == ',' or l[a] == '(':
                    b = 0
                if b == 0:
                    break
                if l[a] > '0' and l[a] < '9':
                    if l[a+1] == '.' and (l[a+2] > 'a' and l[a+2] < 'z' or l[a+2] > 'A' and l[a+2] < 'Z' or l[a+2] == ' ' ):
                        break
                if l[a] == '.':
                    if l[a-1] != str(x) and l[a-1] != '.' and l[a+1] != '.':
                        break
                ret = ret + l[a]
                a = a + 1
                l = l[:temp+1] + ' ' + l[temp+2:]
    print ret



findNotation("http://en.wikipedia.org/wiki/Sicilian_Defence")
