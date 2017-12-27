import xlrd, os

def count(path):
    f_list = os.listdir(path)
    for e in f_list:
        f = e.split('.')
        if f[-1].lower() == 'xls': #转小写str.lower()
            time = get_xls_time(e)
            print(f[0]+"时间为：%d秒"%time)
    pass

def get_xls_time(f_name):
    wb = xlrd.open_workbook(f_name)
    sh = wb.sheet_by_index(0)
    sum = 0
    for i in range(1,sh.nrows):
        value = sh.cell(i,3).value#获取单元格的值
        if value[-1] == '秒':
            sum += int(value[:-1])
        elif value[-1] == '分':
            sum += int(value[:-1])*60
    return sum

if __name__ == '__main__':
    count(os.curdir)