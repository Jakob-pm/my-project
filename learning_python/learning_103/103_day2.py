# date = 03122023
# author = Jakob
print('hello world!')

import xlrd
from xlutils.copy import copy


def main():
    f,c = read_data()
    save(f,c)

def read_data():
    wb = xlrd.open_workbook('/Users/jakob_pc/Desktop/Python实践/数据汇总.xls')
    sh = wb.sheet_by_index(0)
    # global fen_type
    fen_type = {}
    count_price = []

    for r in range(sh.nrows):
        count = sh.cell_value(r,3)*sh.cell_value(r,4)
        count_price.append(count)
        key = sh.cell_value(r,0)
        print('*')
        if fen_type.get(key):
            fen_type[key] +=count
        else:
            fen_type[key] = count

    return fen_type,count_price

def save(fen,count):
    wb = xlrd.open_workbook('/Users/jakob_pc/Desktop/Python实践/数据汇总.xls')
    sh2 = wb.sheet_by_index(0)
    wb2 = copy(wb)
    sh = wb2.get_sheet(0)
    for r in range(sh2.nrows):
        sh.write(r,sh2.ncols,count[r])

    sh3 = wb2.add_sheet('sum_list')
    for i,key in enumerate(fen.keys()):
        sh3.write(i,0,key)
        sh3.write(i,1,fen.get(key))
    wb2.save('/Users/jakob_pc/Desktop/Python实践/数据汇总01.xls')

if __name__ == '__main__':
    main()




print('Goodbye')