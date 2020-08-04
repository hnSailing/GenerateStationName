import requests
import time
from config import stationMap
from bs4 import BeautifulSoup

url = "https://airportcode.51240.com/"

suffix = "__airportcodesou/"

def get_html(url):
    response = requests.get(url)
    return response.text

def analyze_html(html):
    soup = BeautifulSoup(html, "lxml")
    tr = soup.find_all("tr")
    print(tr)
    tr = tr[2]
    tds = tr.find_all('td')
    return tds[1].string,tds[3].string


def store_text(code, name):
    with open('result.txt', 'a')  as f:
        f.write("%s----%s\n"%(code,name))

for v in stationMap.values():
    print("正在进行 %s 三字码对应机场查询...")
    spec_url = url + v + suffix
    #print(spec_url)
    html = get_html(spec_url)
    code, name = analyze_html(html)
    #print(code, name)
    store_text(code, name) 
    time.sleep(2)
