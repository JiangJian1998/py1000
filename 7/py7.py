'''
统计代码行
'''
import os,linecache

sum = 0
type = ['.c','.py','.cpp']#统计的文件类型
ignore_dir = ['venv']#忽略的文件夹名字

def find_code(path):#遍历文件夹下所有文件
    f_list = os.listdir(path)
    for each in f_list:
        current_fp = path+'\\'+each
        if os.path.isfile(current_fp):
            count(current_fp)
        elif os.path.isdir(current_fp):
            if each not in ignore_dir:
                find_code(current_fp)

def count(f_path):
    global sum,type
    f_kz = os.path.splitext(f_path)[1]#分理出文件扩展名
    if f_kz in type:
        try:
            content = linecache.getlines(f_path)
            sum += len(content)
        except:
            pass
        linecache.clearcache()
    else:
        return


if __name__ == '__main__':
    find_code("D:\\代码")
    print("总代码行数为：%d"%sum)