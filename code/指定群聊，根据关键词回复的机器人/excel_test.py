import xlrd


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook('关键词.xls')
    sheet = workbook.sheets()[0]
    row = sheet.nrows  # 行
    col = sheet.ncols  # 列
    print(col)
    print(row)
    keyword = sheet.cell(0, 2).value
    print(keyword)


read_excel()
