from xml.dom.minidom import Document
import xlrd

def xsl_to_xml(f_name, inf):
    doc = Document()
    root = doc.createElement('root')
    doc.appendChild(root)
    student = doc.createElement('student')
    root.appendChild(student)
    com = doc.createComment('学生信息表\n\t\t"id" : [名字, 数学, 语文, 英文]')
    student.appendChild(com)
    student.appendChild(doc.createTextNode('{'))
    for e in inf:
        a = doc.createTextNode('"%s" : ["%s", %s, %s, %s],'%tuple(e))
        student.appendChild(a)
    student.appendChild(doc.createTextNode('}'))
    with open(f_name+'.xml', 'w') as f:
        f.write(doc.toprettyxml())


def get_inf(f_name):
    inf = []
    with xlrd.open_workbook(f_name+'.xls') as f:
        table = f.sheets()[0]
        for i in range(table.nrows):
            inf.append(table.row_values(i))
    return inf

if __name__ == '__main__':
    inf = get_inf("student")
    xsl_to_xml("student", inf)