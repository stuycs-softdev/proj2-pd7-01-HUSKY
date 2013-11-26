import json
import urllib
import urllib2
import sys

page = urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=query&prop=revisions&format=json&rvprop=content&rvlimit=1&titles=Sicilian_Defense)

test = json.load(page);

print test["
