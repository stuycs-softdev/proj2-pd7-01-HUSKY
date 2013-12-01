import json
import urllib2
import unicodedata

def open(link):
    page = urllib2.urlopen(link)
    dict = json.load(page)
    query = dict.keys()[1]
    pages = dict[query]["pages"]
    text = pages.keys()[0]
    l = pages[text]["revisions"][0]["*"]
    a = l.find("1.")
    i = 0
    while i < 5:
        print l[a]
        i = i + 1
        a = a + 1
    


open("http://en.wikipedia.org/w/api.php?action=query&prop=revisions&format=json&rvprop=content&rvlimit=1&titles=Discovered_attack")
