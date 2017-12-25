import urllib.request as urre
import re

def fun():
    url = 'http://www.xfrb.com.cn/html/xiaofeitoutiao/229490.html'
    head = {}
    head ['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3408.400 QQBrowser/9.6.12028.400'
    req = urre.Request(url,headers=head)
    web = urre.urlopen(req)
    t = re.findall( r'<a href="(htt[^>]*?)"' ,web.read().decode())
    try:
        f = open("链接.txt", 'w')
    except:
        print("写入失败")
        exit(-1)
    for each in t:
        f.writelines(each+'\n')
    f.close()
    pass

if __name__ == '__main__':
    fun()