# -*- coding: utf-8 -*-

import xlwt

def sep_file_by_line(filename,line_num,cust_id,is_account,passwd):
    counter = 0
    findex = 1
    file_count = -1
    for file_count, line in enumerate(open(filename, 'r',encoding='utf-8')):
        pass
    file_count += 1
    print(filename + "  共有%s行数据!" % file_count)

    #获取文件名前缀
    file_head = filename.split(".")[0]
    print("文件名前缀是 : " + file_head)

    for line in open(filename, "r",encoding='utf-8'):
        if counter == 0:
            #f = open(file_head + "-" + str(findex) + ".txt", "w",encoding='utf-8')
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('split_result')

            ws.write(0, 0, "服务号码")
            ws.write(0, 1, "UIM卡号(业务不需要时可为空，否则必填)")
            ws.write(0, 2, "CUST_ID")
            ws.write(0, 3, "证件类型(身份证类型为1)")
            ws.write(0, 4, "证件号码")
            ws.write(0, 5, "是否统一账户")
            ws.write(0, 6, "密码")
            findex += 1
        counter += 1
        #f.write(line)
        ws.write(counter - (findex - 2) * line_num, 0, str(line.split()[0]))
        ws.write(counter - (findex - 2) * line_num, 1, str(line.split()[1]))
        ws.write(counter - (findex - 2) * line_num, 2, cust_id)
        ws.write(counter - (findex - 2) * line_num, 5, is_account)
        ws.write(counter - (findex - 2) * line_num, 6, passwd)
        if counter%line_num == 0 and counter != file_count:
            wb.save(file_head + "-" + str(findex - 1) + ".xls")
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('split_result')

            ws.write(0, 0, "服务号码")
            ws.write(0, 1, "UIM卡号(业务不需要时可为空，否则必填)")
            ws.write(0, 2, "CUST_ID")
            ws.write(0, 3, "证件类型(身份证类型为1)")
            ws.write(0, 4, "证件号码")
            ws.write(0, 5, "是否统一账户")
            ws.write(0, 6, "密码")
            #f = open(file_head + "-" + str(findex) + ".txt", "w",encoding='utf-8')
            findex += 1
        wb.save(file_head + "-" + str(findex - 1) + ".xls")

if __name__ == "__main__":
    file_name = str(input("#####请输入源文件名:>>>"))
    line_num = int(input("#####请输入切分行数(切记只能输入数字!!!):>>>"))
    cust_id = str(input("#####请输入CUST_ID的值:>>>"))
    is_account = str(input("#####请输入是否统一账户的值:>>>"))
    passwd = str(input("#####请输入密码的值:>>>"))

    sep_file_by_line(file_name,line_num,cust_id,is_account,passwd)
    print("@@@@@文件切分完成@@@@@")
