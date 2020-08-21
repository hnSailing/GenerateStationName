import requests
import time
from config import station_list
from bs4 import BeautifulSoup
from chardet import detect

url = "https://airport.supfree.net/search.asp?air=%s"


def get_html(url):
    response = requests.get(url)
    response.encoding = "gbk"
    return response.content


def analyze_html(html, code):
    soup = BeautifulSoup(html, "lxml")
    ctable = soup.find_all("table")
    #print(ctable)
    trs = ctable[0].find_all("tr")
    for tr in trs:
        tds = tr.find_all("td")
        if tds[1].string == code:
            name = tds[3].string
            return tds[1].string, name

    return None, None


def store_text(code, name):
    with open('result.txt', 'a')  as f:
        f.write("%s----%s\n"%(code,name))

def store_err_text(code):
    with open('error.txt', 'a') as f:
        f.write("%s 三字码对应机场名未找到\n"%(code))

for i in station_list:
    v = i["code"]
    print("正在进行 %s 三字码对应机场查询..."%(v))
    spec_url = url%(v)
    #print(spec_url)
    html = get_html(spec_url)
    #print(html)
    code, name = analyze_html(html, v)
    #print(code, name)
    #print(code, name)
    if code and name:
        print("三字码: %s 对应机场为: %s"%(code, name))
        store_text(code, name) 
    else:
        print("三字码: %s 对应信息没找到"%(v))
        store_err_text(v)
    time.sleep(0.5)
