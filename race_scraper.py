"""Race Scraper

Race Scraper queries [Athlinks](https://www.athlinks.com/) for race results.
Users can specify a runner they would like to search for, and the program
prints the runner's race results to stdout.
"""

import urllib
from bs4 import BeautifulSoup

runner_name = raw_input("What's the name of your runner? ")

params = urllib.urlencode({'SearchTerm': runner_name})
f = urllib.urlopen("https://www.athlinks.com/result/searchclaim?%s" % params)

html = f.read()

soup = BeautifulSoup(html)

print "Race Name\tDate\tFinish Time"

for row in soup.find_all("tr", { "class":"race-row" }):
    race_name = row.find("a", {"class":["link", "strong"]}).get_text()
    race_date = row.find_all("td")[3].get_text()
    race_time = row.find("td", {"class" : "text-right"}).get_text()
    print "%s\t%s\t%s" % (race_name, race_date, race_time)