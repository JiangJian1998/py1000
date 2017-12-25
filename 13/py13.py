import urllib.request as urre
import re, os
dir_name = '图'#文件夹名称

def pa():
    respond = open_url('http://tieba.baidu.com/p/2166231880')
    img_list = re.findall(r'src="(http://[^"]+)"', respond.read().decode())  # 获取链接

    try:
        if dir_name not in os.listdir('.'):#判断文件夹是否存在
            os.mkdir(dir_name)
        cnt = 0
        for each in img_list:
            if each.split('.')[-1] not in ['jpg', 'png']:#判断后缀名
                continue
            respond = open_url(each)
            f = open(".\\"+dir_name+"\\"+str(cnt)+'.'+each.split('.')[-1], 'wb')#存图片
            f.write(respond.read())
            f.close()
            cnt += 1
    except Exception as e:#打印异常信息
        print(e)
        exit(-1)

def open_url(url):
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4399.400 QQBrowser/9.7.12777.400'
    request = urre.Request(url, headers=head)
    return urre.urlopen(request)


if __name__ == '__main__':
    pa()