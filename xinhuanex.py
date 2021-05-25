from bs4 import BeautifulSoup
import requests
import time

url = 'http://www.xinhuanet.com/politicspro/'

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}


if __name__ == '__main__':
    localtime = time.asctime(time.localtime(time.time()))
    print("当前时间为：", localtime)
    print("[新华社报道源]")
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'
    html = BeautifulSoup(res.text,'html.parser')
    temp = html.find_all(attrs={'class': 'phb_list'})

    for i in temp:
        b = i.find_all('a')
    for i in b:
        print("=>\t{}".format(i.text))