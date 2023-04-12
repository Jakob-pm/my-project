# date = 03102023
# author = Jakob
print('hello world!')

# 01 xlwt 创建excel并写数据

# 终端输入pip3 list，可以查看目前安装的Python库的模块

'''import xlwt

wb = xlwt.Workbook() #Workbook 大写
sh = wb.add_sheet('test_sheet_01')
test_input = input('please add test lines into test file:')
sh.write(0,0,test_input) #行列
wb.save('/Users/jakob_pc/Desktop/Python实践/test_xl_file.csv')'''


# 02 xlrd 读取Excel数据

'''import xlrd

wb = xlrd.open_workbook('/Users/jakob_pc/Desktop/Python实践/test_xl_file.csv')
print(wb.nsheets)# 属性
print(wb.sheet_names()) #方法
# 获取sheet：
sh1 = wb.sheet_by_index(0)
sh2 = wb.sheet_by_name('test_sheet_01')
print(f'sheet里面一共有{sh1.nrows}行{sh1.ncols}列的数据')

print(sh1.cell_value(0,0))
print(sh1.cell(0,0).value)
print(sh1.row(0)[0].value)

print(sh1.row_values(1)) #这样可以获得整行
print(sh1.col_values(1)) #这样可以获得整列

print(type(sh1.col_values(1)))
for i in range(sh1.nrows):
    print(sh1.row_values(i))'''


# 03 xlutils 修改Excel数据
'''import xlrd
import xlwt
from xlutils.copy import copy

read_book = xlrd.open_workbook('/Users/jakob_pc/Desktop/Python实践/test_xl_file.csv')
print(type(read_book)) # <class 'xlrd.book.Book'>
wb = copy(read_book)
print(type(wb)) # <class 'xlwt.Workbook.Workbook'>
sh = wb.get_sheet(0)
print(type(sh)) # <class 'xlwt.Worksheet.Worksheet'>
# sh1 = wb.sheet_by_index(0)
# print(type(sh1))
# 这个问题以后碰到再解决，用get_sheet()方法可以达到目的
# print(sh.cell_value(0,0))

sh.write(9,0,0)
sh.write(9,1,10)
wb.save('/Users/jakob_pc/Desktop/Python实践/test_xl_file.csv')

sh2 = wb.add_sheet('sum_of_sheet03')
read_book = xlrd.open_workbook('/Users/jakob_pc/Desktop/Python实践/test_xl_file.csv')
sh1 = read_book.sheet_by_index(0)
print(type(sh1))
ls1 = sh1.col_values(1)
print(ls1)
res = 0
for i in ls1:
    res += int(i)
print(res)
sh2.write(0,0,'sum01')
sh2.write(0,1,res)
wb.save('/Users/jakob_pc/Desktop/Python实践/test_xl_file.csv')
'''

# 04 xlwt 设置样式

# 官方文档案例
import xlwt
import xlrd
from xlutils.copy import copy

# from datetime import datetime

'''style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write(0, 0, 1234.56, style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))

wb.save('/Users/jakob_pc/Desktop/Python实践/test_xl_file_02.xls')
'''

'''wb = xlwt.Workbook()
sh = wb.add_sheet('A Test Sheet_01')
ft = xlwt.Font()
ft.name = '楷体'
ft.colour_index = 2
ft.height = 16 * 20
ft.bold = True
ft.underline = True
ft.italic = True
style = xlwt.XFStyle()
style.font = ft

# 设置单元格高度：
sh.row(3).height_mismatch = True
sh.row(3).height = 10*256
# 设置单元格宽度：
sh.col(3).width = 20*256

#设置对齐方式
alg = xlwt.Alignment()
alg.horz = 2 # 1左对齐,2居中对齐,3右对齐
alg.vert = 1 # 0上对齐,1居中对齐,2下对齐
style1 = xlwt.XFStyle()
style1.alignment = alg

# 设置背景颜色
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 5
style2 = xlwt.XFStyle()
style2.pattern = pattern



sh.write(0,0,'Test_ori')
sh.write(0,1,'Test_altered',style)
sh.write(3,3,'Test_ano',style1)
sh.write(5,5,'Test_adding',style2)

wb.save('/Users/jakob_pc/Desktop/Python实践/test_xl_file_02.xls')'''

for i in range(1,11):
    ft = xlwt.Font()
    ft.colour_index = i
    print(ft.colour_index)
    style = xlwt.XFStyle()
    style.font = ft
    read_book = xlrd.open_workbook('/Users/jakob_pc/Desktop/Python实践/test_xl_file_03.xls')
    # print(type(read_book))  # <class 'xlrd.book.Book'>
    wb = copy(read_book)
    # print(type(wb))  # <class 'xlwt.Workbook.Workbook'>
    sh = wb.get_sheet(0)
    sh.write(0, i, 'output colour', style)
wb.save('/Users/jakob_pc/Desktop/Python实践/test_xl_file_03.xls')
print('*')


# 05 数据的汇总案例



# 06 表格的拆分
# 07 openpyxl 读取数据
# 08 openpyxl 创建Excel
# 09 多个Excel合并1个Excel中1个sheet
# 10 多个Excel合并1个Excel中多个sheet








print('Goodbye')