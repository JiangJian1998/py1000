def judege(s):
    for e in ban_words:
        if s.find(e) != -1:#find函数返回的是下标，找不到返回-1
            print("Freedom")
            return
    print("Human Rights")

if __name__ == '__main__':
    try:
        f = open("filtered_words.txt", 'r')
    except:
        print("文件读入失败")
        exit(-1)
    ban_words = f.read().split('\n')
    while(True):
        s = input("请输入：")
        judege(s)