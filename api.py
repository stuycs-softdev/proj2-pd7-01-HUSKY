import json
import urllib2

def open(link):
    page = urllib2.urlopen(link)
    dict = json.load(page)
    query = dict.keys()[1]
    pages = dict[query]["pages"]
    text = pages.keys()[0]
    print dict[query]["pages"][text]


open("http://en.wikipedia.org/w/api.php?action=query&prop=revisions&format=json&rvprop=content&rvlimit=1&titles=Discovered_attack")
