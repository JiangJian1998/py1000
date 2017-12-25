import urllib.request as urre
import socket, time, re
def test():

    url = 'http://202.103.141.243:8081/Jwweb/'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4399.400 QQBrowser/9.7.12777.400'
    socket.setdefaulttimeout(4)#超时设置
    request = urre.Request(url, headers=head)
    while(True):
        time.sleep(30)
        try:
            repon = urre.urlopen(request)
        except:
            print('超时')
            continue
        print(repon.getcode())
        s = re.findall('<center><.*>(.+)</font></center>', repon.read().decode('gbk'))
        print(s)


    pass


if __name__ == '__main__':
    test()

