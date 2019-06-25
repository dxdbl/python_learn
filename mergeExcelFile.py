# coding:utf-8
####################################################
# 程序功能 :
# 程序运行说明 : 合并目录下的xls文档，生成合并后的xls文档
# 作者 : mhf @ 2019-06-25
# 版本 : V1.0
# 修改时间 :
# 修改人 :
# 修改内容 :
####################################################
import os
import xlrd,xlwt

#列出目录下的文件
def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.xls':
                L.append(os.path.join(root, file))
    return L
def read_excel(filepath):
    # 打开文件
    workbook = xlrd.open_workbook(filepath)
    # 获取所有sheet
    print(workbook.sheet_names())  # [u'sheet1', u'sheet2']

    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始

    # sheet的名称，行数，列数
    sheet_name=sheet1.name
    sheet_rows_num=sheet1.nrows
    sheet_cols_num=sheet1.ncols
    print(sheet_name, sheet_rows_num,sheet_cols_num)

    # 获取整行和整列的值（数组）
    for i in range(sheet_rows_num):
        rows = sheet1.row_values(i)
        print(rows)

    # 获取单元格内容
    #print(sheet1.cell(1, 0).value.encode('utf-8'))
    #print(sheet1.cell_value(1, 0).encode('utf-8'))
    #print(sheet1.row(1)[0].value.encode('utf-8'))

    # 获取单元格内容的数据类型
    #print(sheet1.cell(1, 0).ctype)



if __name__ == '__main__':
    file = file_name("D:\\A\\b")
    for f in file:
        print(f)
        excel_content = read_excel("D:\\A\\b\\系统导出未改变过的.xls")
        print(excel_content)

























