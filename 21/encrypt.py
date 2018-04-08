import hashlib, os, hmac

def encrypty(password, salt=None):
    if salt is None:
        salt = os.urandom(8) #8字节随机 64位
    assert len(salt) == 8 #检查错误，表达式为真继续执行，否则报错
    #assert isinstance(salt, str)
    en_password = password.encode('utf-8') #encode编码，decode解码
    for i in range(10):#10重加密
        en_password = hmac.HMAC(en_password, salt, hashlib.sha256).digest()
    return salt+en_password#比特位串，前八字节是salt

def check(en_password, password):#此加密不能找到明文
    return en_password == encrypty(password,salt=en_password[:8])
    pass

password = input("请输入密码：")
encrypted_password = encrypty(password)
while check(encrypted_password, input("请输入密码:")) != True:
    pass