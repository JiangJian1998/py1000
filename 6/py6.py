'''
统计重要的词
'''
import os,re

ignore_word = ['a','the','I','am','is','are','so','So']

def count(path):
    f_list = os.listdir(path)
    for each_f in f_list:
        if each_f[-4:] == ".txt":#4是从后记起要截取的字符数
            try:
                f = open(path+'\\'+each_f, 'r')
            except:
                print("文件打开失败！")
                exit(-1)
            s = f.read()
            s = re.split(r'[.\s;,?:]',s)#多分割
            try:
                while(1):
                    s.remove('')#除去空白
            except:
                pass
            word = set(s)
            for each in word:
                if each not in ignore_word:
                    cnt = s.count(each)
                    n_f = open(path+'\\n_'+each_f, "a+")
                    n_f.writelines("%s %d\n"%(each, cnt))#格式是""%元组


if __name__ == '__main__':
    count(".\\dir")