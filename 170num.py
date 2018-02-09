# coding:utf-8
####################################################
# 程序功能 :
# 程序运行说明 : 读取目录下的test.txt文档，生成结果文档
# 作者 : mhf @ 2018-02-08
# 版本 : V1.1
# 修改时间 : 2018-02-09 13:37
# 修改人 : mhf
####################################################
import re
import string
import time
import os

#检查文件名时候重复函数
def check_filename_available(filename):
    n=[0]
    def check_meta(file_name):
        file_name_new=file_name
        if os.path.isfile(file_name):
            file_name_new=file_name[:file_name.rfind('.')]+'_'+str(n[0])+file_name[file_name.rfind('.'):]
            n[0]+=1
        if os.path.isfile(file_name_new):
            file_name_new=check_meta(file_name)
        return file_name_new
    return_name=check_meta(filename)
    return return_name

#定义处理函数
def list_num(phone_num, start_str, end_str):
    #获取系统当前时间
    now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(now_time)

    #打开文件准备接收结果
    f = open(check_filename_available("%s.txt" % phone_num), 'a')

    #处理开始ICCID
    print(re.findall(r"\d+\.?\d*",start_str))
    start_str_tail_str = re.findall(r"\d+\.?\d*",start_str)[-1]
    print(start_str_tail_str)
    tail_str_len = len(start_str_tail_str)
    print(tail_str_len)
    start_str_tail_num = int(re.findall(r"\d+\.?\d*",start_str)[-1])
    start_str_tail_num_len = len(str(start_str_tail_num))
    print(start_str_tail_num)
    print(start_str_tail_num_len)
    start_str_head = start_str.rstrip(string.digits)
    print(start_str_head)

    #处理结束ICCID
    print(re.findall(r"\d+\.?\d*",end_str))
    end_str_tail_num = int(re.findall(r"\d+\.?\d*",end_str)[-1])
    print(end_str_tail_num)
    end_str_head = end_str.rstrip(string.digits)
    print(end_str_head)
    #循环遍历,根据末尾数字长度进行前面数字0的填充
    while start_str_tail_num <= end_str_tail_num:
        print(phone_num + "    " + start_str_head + str(start_str_tail_num).zfill(tail_str_len))
        f.write(phone_num + "    " + start_str_head + str(start_str_tail_num).zfill(tail_str_len) + "\n")
        start_str_tail_num += 1
    f.close()

#读取文件进行处理，输出结果到txt文档
for line in open("test.txt","r"):
    print(line.split())
    phone_num = line.split()[0]
    print(phone_num)
    start_iccid = line.split()[1]
    print(start_iccid)
    end_iccid = line.split()[2]
    print(end_iccid)
    #调用输出函数
    list_num(phone_num,start_iccid,end_iccid)

    
