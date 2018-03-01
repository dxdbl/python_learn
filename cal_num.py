# coding:utf-8
###################################################
# 程序功能 :
# 程序运行说明 : 计算首尾iccid的个数
# 作者 : mhf @ 2018-03-01
# 版本 : V1.0
# 修改时间 :
# 修改人 :
####################################################
import re
import time
import sys

#定义处理函数
def cal_num(start,end):
    #打开文件准备接收结果
    f = open("cal_result.txt","a")

    #处理开始ICCID
    start_tail_num = int(re.findall(r"\d+\.?\d*",start)[-1])
    #处理结束iccid
    end_tail_num = int(re.findall(r"\d+\.?\d*",end)[-1])
    #计算首尾iccid的个数
    cal_res= end_tail_num - start_tail_num + 1
    print("首到尾个数为:" + str(cal_res))
    #把结果写入文件
    f.write(start + "    " + end + "    " + str(cal_res) + "\n")
    f.close()

#脚本执行
#判断传入参数个数
if len(sys.argv) != 2:
    print("error!" + "\n" + "格式如下:" + "\n" + "python cal_num.py filename")
    print("其中filename是需要操作的原始txt文档,例如: cal.txt" + "\n")
    exit()
# 传参数
filename = sys.argv[1]
try:
    # 获取系统当前时间
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("程序运行时间:" + now_time)
    # 读取文件进行处理，输出结果到txt文档
    for line in open(filename, "r"):
        print("----------ICCID组分割线----------")
        start_iccid = line.split()[0]
        print("开始ICCID:"+ start_iccid)
        end_iccid = line.split()[1]
        print("结束ICCID:" + end_iccid)
        # 调用输出函数
        cal_num(start_iccid, end_iccid)
except:
    print("出现意外,程序结束,请检查输入是否正确!")
