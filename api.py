import json
import urllib2
import unicodedata

def findNotation(link):
    page = urllib2.urlopen(link)
    dict = json.load(page)
    query = dict.keys()[1]
    pages = dict[query]["pages"]
    text = pages.keys()[0]
    l = pages[text]["revisions"][0]["*"]
    ret = ""
    for x in range(1,100):
        a = l.find(str(x)+'.')
        ret = ret + l[a]
        a = a + 1
        b = 1
        if (l[a] > '9' and l[a] < 'x') or l[a] > 'x' or (l[a] < '0' and l[a] > '.') or (l[a] < '.' and l[a] > ' ') or l[a] < ' ' or l[a] == '}':
                if (l[a+1] > '9' and l[a+1] < 'x') or l[a+1] > 'x' or (l[a+1] < '0' and l[a+1] > '.') or (l[a+1] < '.' and l[a+1] > ' ') or l[a+1] < ' ' or l[a+1] == '}':
                    break
        while b != 0:
            if (l[a] > '9' and l[a] < 'x') or l[a] > 'x' or (l[a] < '0' and l[a] > '.') or (l[a] < '.' and l[a] > ' ') or l[a] < ' ' or l[a] == '}':
                if (l[a+1] > '9' and l[a+1] < 'x') or l[a+1] > 'x' or (l[a+1] < '0' and l[a+1] > '.') or (l[a+1] < '.' and l[a+1] > ' ') or l[a+1] < ' ' or l[a+1] == '}':
                    b = 0
            if b == 0:
                break
            ret = ret + l[a]
            a = a + 1    
    print ret
    
    


findNotation("http://en.wikipedia.org/w/api.php?action=query&prop=revisions&format=json&rvprop=content&rvlimit=1&titles=Discovered_attack")
