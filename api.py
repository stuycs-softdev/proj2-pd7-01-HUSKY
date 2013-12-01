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
        if (l[a] > '9' and l[a] < 'A') or (l[a] > 'A' and l[a] < 'Z') or (l[a] > 'Z' and l[a] < 'a') or (l[a] > 'a' and l[a] < 'z') or l[a] > 'z' or (l[a] < '0' and l[a] > '.') or (l[a] < '.' and l[a] > ' ') or l[a] < ' ' or l[a] == '}':
            if (l[a+1] > '9' and l[a+1] < 'A') or (l[a+1] > 'A' and l[a+1] < 'Z') or (l[a+1] > 'Z' and l[a+1] < 'a') or (l[a+1] > 'a' and l[a+1] < 'x') or l[a+1] > 'x' or (l[a+1] < '0' and l[a+1] > '.') or (l[a+1] < '.' and l[a+1] > ' ') or l[a+1] < ' ' or l[a+1] == '}':
                if (l[a+2] > '9' and l[a+2] < 'A') or (l[a+2] > 'A' and l[a+2] < 'Z') or (l[a+2] > 'Z' and l[a+2] < 'a') or (l[a+2] > 'a' and l[a+2] < 'x') or l[a+2] > 'x' or (l[a+2] < '0' and l[a+2] > '.') or (l[a+2] < '.' and l[a+2] > ' ') or l[a+2] < ' ' or l[a+2] == '}':
                        if (l[a+3] > '9' and l[a+3] < 'A') or (l[a+3] > 'A' and l[a+3] < 'Z') or (l[a+3] > 'Z' and l[a+3] < 'a') or (l[a+3] > 'a' and l[a+3] < 'x') or l[a+3] > 'x' or (l[a+3] < '0' and l[a+3] > '.') or (l[a+3] < '.' and l[a+3] > ' ') or l[a+3] < ' ' or l[a+3] == '}':
                            break
        while b != 0:
            if (l[a] > '9' and l[a] < 'A') or (l[a] > 'A' and l[a] < 'Z') or (l[a] > 'Z' and l[a] < 'a') or (l[a] > 'a' and l[a] < 'z') or l[a] > 'z' or (l[a] < '0' and l[a] > '.') or (l[a] < '.' and l[a] > ' ') or l[a] < ' ' or l[a] == '}':
                if (l[a+1] > '9' and l[a+1] < 'A') or (l[a+1] > 'A' and l[a+1] < 'Z') or (l[a+1] > 'Z' and l[a+1] < 'a') or (l[a+1] > 'a' and l[a+1] < 'z') or l[a+1] > 'z' or (l[a+1] < '0' and l[a+1] > '.') or (l[a+1] < '.' and l[a+1] > ' ') or l[a+1] < ' ' or l[a+1] == '}':
                    if (l[a+2] > '9' and l[a+2] < 'A') or (l[a+2] > 'A' and l[a+2] < 'Z') or (l[a+2] > 'Z' and l[a+2] < 'a') or (l[a+2] > 'a' and l[a+2] < 'x') or l[a+2] > 'x' or (l[a+2] < '0' and l[a+2] > '.') or (l[a+2] < '.' and l[a+2] > ' ') or l[a+2] < ' ' or l[a+2] == '}':
                        if (l[a+3] > '9' and l[a+3] < 'A') or (l[a+3] > 'A' and l[a+3] < 'Z') or (l[a+3] > 'Z' and l[a+3] < 'a') or (l[a+3] > 'a' and l[a+3] < 'x') or l[a+3] > 'x' or (l[a+3] < '0' and l[a+3] > '.') or (l[a+3] < '.' and l[a+3] > ' ') or l[a+3] < ' ' or l[a+3] == '}':
                            b = 0
            if b == 0:
                break
            ret = ret + l[a]
            a = a + 1    
    print ret
       
   
    
    


findNotation("http://en.wikipedia.org/w/api.php?action=query&prop=revisions&format=json&rvprop=content&rvlimit=1&titles=Discovered_attack")
