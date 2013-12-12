import json
import urllib2
import unicodedata

def isMove(string):
    num = False
    alpha = False
    other = False
    for x in string:
        if x.isdigit():
            num = True
        if x.isalpha():
            alpha = True
        if (x >= '!' and x <= '*') or (x > '9' and x < '?') or (x > 'Z' and x < 'a') or (x > 'z' and x <= '~') or x == '@' or x == '-' or x == '/':
            other = True
    return num and alpha and not other

def cleanMoves(string):
    if string[1:2] == '.':
        string = string[2:]
    i = len(string) - 1
    while (1):
        s = string[i:i+1]
        if (s > ' ' and s < '0') or (s > '9' and s < 'A'):
            string = string[:i]
            i = i - 1
        else:
            break
    i = 0
    while (1):
        s = string[i:i+1]
        if (s > ' ' and s < '0') or (s > '9' and s < 'A'):
            string = string[i+1:]
        else:
            break
    return string

def findNotation(link):
    path = link[link.find("/wiki/")+6:]
    page = urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=query&prop=revisions&format=json&rvprop=content&rvlimit=1&titles=" + path)
    dict = json.load(page)
    query = dict.keys()[1]
    pages = dict[query]["pages"]
    text = pages.keys()[0]
    c = pages[text]["revisions"][0]["*"]
    f = c.encode('utf-8','ignore')
    d = f.__len__()
    e = f.find('1.')   
    l = f[e:]
    l = l.split()
    moves = []    
    for x in l:
        if isMove(x):
            moves.append(x)
    x = 0
    final = []
    m1 = ''
    m2 = ''
    while (x < len(moves) - 1):
        m1 = moves[x][1:2]
        m2 = moves[x+1][1:2]
        if m1 == '.':
            if m2 != '.':
                chess = moves[x] + ' ' + moves[x+1]
                final.append(cleanMoves(chess))
                x = x + 2
            elif m2 == '.':
                final.append(cleanMoves(moves[x]))
                final.append(cleanMoves(moves[x+1]))
                x = x + 2
            else:
                x = x + 1
    return final

