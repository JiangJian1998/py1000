import string
def find(filename):
    #处理文件打开异常
    try:
        f = open(filename, 'r')
    except:
        print("打开文件失败")
        exit(1)
    s = f.read()#返回字符串
    flag = sum = 0
    #统计词数
    for i in range(len(s)):
        if (s[i] in string.ascii_letters):
            flag = 1
        elif (s[i] not in string.ascii_letters and flag==1):
            flag = 0
            sum += 1
    print(sum)
if __name__ == '__main__':
    find('eng.txt')