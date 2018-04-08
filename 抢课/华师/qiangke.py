import requests

def main():
    u = "https://jwc.scnu.edu.cn/default2.aspx"
    jwc_url = "https://jwc.scnu.edu.cn/"
    yzm_url = "https://jwc.scnu.edu.cn/CheckCode.aspx"
    data ={'txtUserName':'20172005097','TextBox2':'j84491135'}

    n = requests.get(yzm_url)
    with open("code.jpg", 'wb') as f:
        f.write(n.content)
        f.close()

    code = input("验证码：")
    data['txtSecretCode']=str(code)
    r = requests.post(u, data=data)
    print(r.text)

if __name__ == '__main__':
    main()