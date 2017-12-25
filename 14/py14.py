import xlwt, re

def change(f_name):
    try:
        f = open(f_name, 'r', encoding='utf-8')#不写encoding会乱码
    except:
        print("打开文件失败")
        exit(-1)
    find = re.findall(r'"(\d+)":\["(.+)",(\d+),(\d+),(\d+)\]',f.read())   #[]要用\   匹配的内容放在()   数字[0-9] = \d
    #"1":["张三",150,120,100]
    wb = xlwt.Workbook()#创建工作簿就是excel
    ws = wb.add_sheet(f_name.split('.')[0])#创建表  返回表对象        文件全名.split('.')[0]  返回文件名
    for i in range(len(find)):
        ws.write(i, 0, find[i][0])
        ws.write(i, 1, find[i][1])
        ws.write(i, 2, find[i][2])
        ws.write(i, 3, find[i][3])
        ws.write(i, 4, find[i][4])
    wb.save(f_name.split('.')[0] + '.xls')#保存excel  后缀名是xls
    pass


if __name__ == '__main__':
    change("student.txt")