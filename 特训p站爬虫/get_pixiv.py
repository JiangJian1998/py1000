'''
功能：爬取p站图片  未完成  难点 网页js渲染
'''
import urllib.request as urre
import re
import urllib.parse


def get_rank_photo():
    login_url = 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'
    url = 'https://i.pximg.net/img-original/img/2017/12/19/08/07/17/66351742_p0.jpg'
    rank_url = 'https://www.pixiv.net/ranking.php?mode=daily&date=20171219'
#header
    head = {}
    head ['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4399.400 QQBrowser/9.7.12777.400'
    head ['Referer'] = 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'
#find postkey
    request = urre.Request(login_url,headers=head)
    response = urre.urlopen(request)
    html = response.read().decode()
    key = re.findall(r'"pixivAccount.postKey":"(.*?)"',html)
#data
    data = {}
    data ['pixiv_id'] = '1197749258'
    data ['password'] = '84491135'
    data ['post_key'] = str(key[0])
    data ['source'] = 'pc'
    data ['ref'] = 'wwwtop_accounts_index'
    data ['return_to'] = 'https://www.pixiv.net/ranking.php?mode=daily&date=20171219'
    data = urllib.parse.urlencode(data).encode('utf-8')
#login
    request = urre.Request(login_url, data, headers=head)
    response = urre.urlopen(request)
    print(response.read().decode())
    pass

'''
    img_head = head
    img_head ['Referer'] = 'https://i.pximg.net/img-original/img/2017/12/18/00/56/22/66337051_p0.png'
    img_req = urre.Request(url, headers=img_head)
    img_res = urre.urlopen(img_req)
    img = img_res.read()
    f = open("a.jpg", 'wb')
    f.write(img)
    f.close()
'''




if __name__ == '__main__':
    get_rank_photo()