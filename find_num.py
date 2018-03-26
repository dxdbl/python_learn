#-*- coding:utf-8 -*-
######################################################
# 程序功能 :
# 程序运行说明 :例如：python num_set.py test.txt 1706241
# 作者 : mhf @ 2018-03-22
# 版本 : V1.0
# 修改时间 :
# 修改人 :
#######################################################
import time
import re
import string


#定义处理函数
def end_add_num(line,num):
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

    #循环遍历,根据本身数字长度进行前面数字0的填充
    if tail_str_len == line_tail_num_len:
        print(line_head + str(line_tail_num))
        print(line + "    ")
        print(line_head + str(line_tail_num_add_1) + "\n")
        return (line_head + str(line_tail_num_add_1))
    else:
        print("数字前面含有数字0!")
        print(line + "    ")
        print(line_head + str(line_tail_num_add_1).zfill(tail_str_len) + "\n")
        return (line_head + str(line_tail_num_add_1).zfill(tail_str_len))

#脚本执行
# 先清空临时文件
f100 = open("tmp.txt", "w+", encoding='utf-8')
f100.truncate()
f100.close()

f101 = open("find_num_result.txt", "w+", encoding='utf-8')
f101.truncate()
f101.close()

#file1 = "test1.txt"
file1 = input("请输入文档1的文件名:例如:test1.txt \n")
#file2 = "test2.txt"
file2 = input("请输入文档2的文件名:例如:test1.txt \n")
try:
    # 获取系统当前时间
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("程序运行时间:" + now_time)
    print("###################################")
    #打开文件等待接收结果
    f = open("find_num_result.txt","a",encoding='utf-8')
    # 读取文件进行处理，输出结果到txt文档
    for line in open(file1, "r",encoding='utf-8'):
        num_head = line.split()[0]
        num_sum = line.split()[1]
        print(num_head)
        print(num_sum)
        # 置flag为1,即默认是不带汉字可以累加的情况
        flag = 1
        for line2 in open(file2,"r",encoding='utf-8'):
            num_head_2 = line2.split()[0]
            start_iccid = line2.split()[1]
            end_iccid = line2.split()[2]
            num_iccid = line2.split()[3]
            if num_head == num_head_2 and (len(start_iccid) > 20 or len(end_iccid) > 20):
                flag = 0
                print("flag = " + str(flag))
        #flag为1,不含有汉字，进行计算
        if flag == 1:
            print("可以累加！")
            #把要计算累加的数据放到临时文件中
            f2 = open("tmp.txt","a",encoding='utf-8')
            for line3 in open(file2, "r", encoding='utf-8'):
                num_head_3 = line3.split()[0]
                if num_head == num_head_3:
                    f2.write(line3)
            f2.close()
            num_sum_99 = 0
            for line99 in open("tmp.txt", "r", encoding='utf-8'):
                num_head_99 = line99.split()[0]
                num_sub_99 = line99.split()[3]
                if num_head == num_head_99:
                    num_sum_99 = num_sum_99 + int(num_sub_99)
            print(num_sum_99)
            num_left = int(num_sum)
            for line5 in open("tmp.txt", "r", encoding='utf-8'):
                num_head_5 = line5.split()[0]
                start_iccid_5 = line5.split()[1]
                end_iccid_5 = line5.split()[2]
                num_sum_sub = line5.split()[3]
                if num_head_5 == num_head and int(num_sum) == num_sum_99:
                    f.write(line5.strip('\n') + "        " + "共取" + num_sum + "数量正好!\n" )
                elif num_head_5 == num_head and int(num_sum) > num_sum_99:
                    f.write(line5.strip('\n') + "        " + "共取" + str(num_sum_99) + "还差#-" + str(int(num_sum) - int(num_sum_99)) + "-#个\n")
                elif num_head_5 == num_head and int(num_sum) < num_sum_99:
                    num_left = num_left - int(num_sum_sub)
                    if num_left > 0:
                        print(num_left)
                        f.write(line5.strip('\n') + "        " + "共取" + num_sum + ",此行已取" + num_sum_sub + "个!\n")
                    if num_left <= 0:
                        add_num = int(num_sum_sub)-abs(num_left)
                        print(add_num)
                        print(line5.strip('\n') + "在这一行里面取" + str(add_num) + "个数:\n")
                        end_iccid_5_final = end_add_num(start_iccid_5,add_num - 1)
                        print(end_iccid_5_final)
                        f.write(num_head_5 + " " + start_iccid_5 + "    " + end_iccid_5_final + "    " + str(add_num) + "        " + "此行取" + str(add_num) + "个数即可!已取完!共取" + num_sum + "个!\n")
                        break
        # flag为0,含有汉字，不进行计算原样输出
        else:
            print("含有中文不累加！")
            for line4 in open(file2, "r", encoding='utf-8'):
                num_head_4 = line4.split()[0]
                if num_head == num_head_4:
                    f.write(line4.strip('\n') + "    " + "###请注意,该号段需手工处理!###\n")
    f.close()
    print("###################################")
    print("查找结束,结果保存在find_num_result.txt中\n")
except:
    print("出现意外,程序结束,请检查输入是否正确!")
