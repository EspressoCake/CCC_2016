import requests
from BeautifulSoup import BeautifulSoup
import subprocess
import os
import re
import sys

def main():
    initial_URL = "http://mirror.netcologne.de/CCC/congress/2016/h264-hd/"
    request = requests.get(initial_URL)
    soup = BeautifulSoup(request.text)
    urls = [a['href'] for a in soup.findAll('a', href=True) if "-eng-" in a['href'] and "-deu-" not in a['href']]
    for item in urls:
        regex = re.compile("^33c3.\d+.eng.")
        if os.path.isfile(re.sub(regex, "33C3_", item)):
            continue
        else:
            print "Getting Item: %s" % (item)
            wget = initial_URL + item
            os.system('aria2c -x16 %s -o %s >/dev/null 2>&1' % (wget, re.sub(regex, "33C3_", item)))

main()
