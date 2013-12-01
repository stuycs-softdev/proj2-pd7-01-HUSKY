import json
import bs4
import urllib2
import sys


page = urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=query&prop=revisions&format=json&rvprop=content&rvlimit=1&titles=Sicilian_Defence")

test = json.load(page)
print(test)
