import requests
from BeautifulSoup import BeautifulSoup
import subprocess
import os

def main():
    initial_URL = "http://mirror.netcologne.de/CCC/congress/2016/h264-hd/"
    request = requests.get(initial_URL)
    soup = BeautifulSoup(request.text)
    urls = [a['href'] for a in soup.findAll('a', href=True) if "-eng-" in a['href'] and "-deu-" not in a['href']]
    for item in urls:
        if os.path.isfile(item):
            continue
        else:
            wget = initial_URL + item
            os.system('aria2c -x16 %s' % (wget))
            print item
main()
