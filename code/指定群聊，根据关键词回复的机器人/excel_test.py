import xlrd


def get_reply(content):
    # 打开文件
    workbook = xlrd.open_workbook('关键词.xls')
    sheet = workbook.sheets()[0]
    row = sheet.nrows  # 一共有多少行
    reply = '-----'
    for r in range(1, row):
        print(sheet.cell(r, 0).value)
        if sheet.cell(r, 0).value in content:
            reply = sheet.cell(r, 2).value
    return reply


res = get_reply('这是一条测试语句')
print(res)
