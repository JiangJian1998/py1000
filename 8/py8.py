'''
抓取网页内容   未完成
'''
import urllib.request as urre
import bs4 as bs
import re

def fund():
    url = 'http://www.xfrb.com.cn/html/xiaofeitoutiao/229490.html'
    head = {}
    head ['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3408.400 QQBrowser/9.6.12028.400'
    req = urre.Request(url,headers=head)
    re_web = urre.urlopen(req)
    try:
        f = open("正文.txt", 'w', encoding='utf-8')#用utf-8打开文件方便保存网页源代码
    except:
        print("保存文件失败")
        exit(-1)
    soup = bs.BeautifulSoup(re_web.read().decode(),'html.parser')#read完后要解码

    f.writelines(str(soup.contents))
    # find = soup.find_all(["p", "li", "h"])
    # find = soup.find(text=re.compile(r"<p*>*</p>"))
    # re.compile(r'>^*<', find)
    print(re.findall(r'<a.*>(.*?)</a>', str(soup.contents)))
    f.close()
    pass

if __name__ == '__main__':
    fund();