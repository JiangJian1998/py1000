ban_words = []
def load_ban_words():
    global  ban_words
    try:
        f = open("filtered_words.txt", 'r')
    except:
        print("文件读入失败")
        exit(-1)
    ban_words = f.read().split('\n')

def words_replace(s):
    for each_word in ban_words:
        s = s.replace(each_word, '*'*len(each_word))
    return s

if __name__ == '__main__':
    load_ban_words()
    while(True):
        while(True):
            s = input("请输入:")
            if (s == 'q'):  #判断是否退出程序
                ans = input('是否退出[Y/N]:')
                if ans.lower() == 'y' or ans.lower() == 'n':
                    if ans.lower() == 'y':
                        exit(0)
                    else:
                        continue
            else:
                break
        s = words_replace(s)
        print(s)