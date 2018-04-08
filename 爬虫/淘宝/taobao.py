import requests, re

def getHtml(url):
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3408.400 QQBrowser/9.6.12028.400'
    r = requests.get(url, headers=head)
    return r

def getInfo(info_list, html):
    price = re.findall(r'"view_price":"([^"]+)"', html.text)
    title = re.findall(r'"raw_title":"([^"]+)"', html.text)
    sale = re.findall(r'"view_sales":"([^"]+)"', html.text)
    location = re.findall(r'"item_loc":"([^"]+)"', html.text)
    for i in range(len(price)):
        info_list.append([title[i],price[i],sale[i],location[i]])

if __name__ == '__main__':
    goods = '硬盘'
    depth = 2
    url = 'https://s.taobao.com/search?q=' + goods
    info_list = []
    for i in range(depth):
        html = getHtml(url+'&s='+str(44*i))
        getInfo(info_list, html)
    print("{:50}{:20}{:20}{:20}".format('商品','价格','销量','坐标'))
    for i in range(len(info_list)):
        print("{:<50}{:<20}{:<20}{:<20}".format(info_list[i][0],info_list[i][1],info_list[i][2],info_list[i][3]))

