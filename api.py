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
    h = l.find('==')
    l = l[:h]
    l = l.split()
    ans = []
    for x in l:
        if isMove(x):
            ans.append(x)
    for x in ans:
        print x
#finds the algebraic notation
      


findNotation("http://en.wikipedia.org/wiki/Sicilian_Defence")
