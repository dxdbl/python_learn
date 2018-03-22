# coding:utf-8
######################################################
# 程序功能 :
# 程序运行说明 :例如：python num_set.py test.txt 1706241
# 作者 : mhf @ 2018-03-22
# 版本 : V1.0
# 修改时间 :
# 修改人 :
#######################################################
import time
import sys

#脚本执行
#判断传入参数个数
if len(sys.argv) != 3:
    print("error!" + "\n" + "格式如下:" + "\n" + "python cal_num.py filename")
    print("其中filename是需要操作的原始txt文档,例如: cal.txt" + "\n")
    exit()
# 传参数
filename = sys.argv[1]
num_head = sys.argv[2]
try:
    # 获取系统当前时间
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("程序运行时间:" + now_time)
    #打开文件等待接收结果
    f = open("%s.txt" % num_head,"a")
    # 读取文件进行处理，输出结果到txt文档
    for line in open(filename, "r",encoding='utf-8'):
        print("---正在查找号段%s......---" %  num_head)
        num_str = line.split()[0]
        if num_str == num_head:
            f.write(line)
    f.close()
    print("##################################")
    print("查找结束,结果保存在%s.txt中" % num_head)
except:
    print("出现意外,程序结束,请检查输入是否正确!")
