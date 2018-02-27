# coding:utf-8
####################################################
# 程序功能 :
# 程序运行说明 : 尾号加(num -1)输出新iccid
# 作者 : mhf @ 2018-02-27
# 版本 : V1.0
# 修改时间 :
# 修改人 : mhf
####################################################
import re
import string
import time
import sys

#定义处理函数
def end_add_num(line,num):
    #打开文件准备接收结果
    f = open("end_result.txt","a")

    #处理开始ICCID
    print(re.findall(r"\d+\.?\d*",line))
    line_tail_str = re.findall(r"\d+\.?\d*",line)[-1]
    print(line_tail_str)
    tail_str_len = len(line_tail_str)
    print(tail_str_len)
    line_tail_num = int(re.findall(r"\d+\.?\d*",line)[-1])
    line_tail_num_add_1 = line_tail_num + num
    line_tail_num_len = len(str(line_tail_num))
    print(line_tail_num)
    print(line_tail_num_len)
    line_head = line.rstrip(string.digits)
    print(line_head)

    #根据本身数字长度进行前面数字0的填充
    if tail_str_len == line_tail_num_len:
        print(line_head + str(line_tail_num))
        f.write(line + "  ")
        f.write(line_head + str(line_tail_num_add_1) + "\n")
    else:
        print("数字前面含有数字0!")
        f.write(line + "  ")
        f.write(line_head + str(line_tail_num_add_1).zfill(tail_str_len) + "\n")

    f.close()

#脚本执行
#判断传入参数个数
if len(sys.argv) != 2:
    print("error!" + "\n" + "格式如下:" + "\n" + "python end_add_num.py filename")
    print("其中filename是需要操作的原始txt文档,例如: end.txt" + "\n")
    exit()
# 传参数
filename = sys.argv[1]
try:
    # 读取文件进行处理，输出结果到txt文档
    for line in open(filename, "r"):
        print(line.split())
        start_iccid = line.split()[0]
        add_num  = int(line.split()[1]) - 1
        print(start_iccid)
        # 获取系统当前时间
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print("程序运行时间:" + now_time)
        # 调用输出函数
        end_add_num(start_iccid,add_num)
except:
    print("出现意外,程序结束,请检查输入是否正确!")
