import string, random
keylen = 20
def create():
    seq = string.ascii_letters + string.digits#包含了字母和数字的列表
    f = open('key.txt','w+')#w+读写模式，若不存在则创建，存在则清空。  a+是追加
    for i in range(200):
        t = random.choices(seq,k=keylen)#k是返回的长度
        f.writelines(t)
        f.writelines('\r')#手动回车，t是列表不能转成字符串
    f.close()

if __name__ == '__main__':
    create()