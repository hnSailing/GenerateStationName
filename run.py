import requests
import time
from config import stationMap
from bs4 import BeautifulSoup

url = "https://airportcode.51240.com/"

suffix = "__airportcodesou/"

def get_html(url):
    response = requests.get(url)
    return response.text

def analyze_html(html, code):
    soup = BeautifulSoup(html, "lxml")
    trs = soup.find_all("tr")
    if len(trs) < 3:
        return None, None
    for tr in trs:
        td = tr.find_all('td')
        if td[1].string == code:
            #print(td[1].string, td[3].string)
            return td[1].string, td[3].string
    return None,None


def store_text(code, name):
    with open('result.txt', 'a')  as f:
        f.write("%s----%s\n"%(code,name))

def store_err_text(code):
    with open('error.txt', 'a') as f:
        f.write("%s 三字码对应机场名未找到\n"%(code))

for v in stationMap.values():
    print("正在进行 %s 三字码对应机场查询..."%(v))
    spec_url = url + v + suffix
    #print(spec_url)
    html = get_html(spec_url)
    code, name = analyze_html(html, v)
    #print(code, name)
    if code and name:
        print("三字码: %s 对应机场为: %s"%(code, name))
        store_text(code, name) 
    else:
        print("三字码: %s 对应信息没找到"%(v))
        store_err_text(v)
    time.sleep(2)
