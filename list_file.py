# -*- coding: utf-8 -*-
import os
import sys

# 列出文件夹名称或者文件名(带后缀名)
def list_file(path):
    file_name_or_path_name = os.listdir(path)
    return file_name_or_path_name

# 查找目录下面相关后缀文件
def acc_suffix(name,suffix):
    f = open("yuntiqu.log", "a")
    if (name.split(".")[-1] == suffix and len(name.split(".")) != 1 ):
        print(name)
        f.write(name + "\n")
    elif ((len(name.split(".")) == 1) and suffix == "0"):
        print(name)
        f.write(name + "\n")
    f.close()
#主程序入口
list_any = list_file(".")

#判断参数个数
if (len(sys.argv) != 2):
    print("###########################################")
    print("########参数个数不对!#######################")
    print("########参数代表意义:#######################")
    print("########0代表获取文件夹名称##################")
    print("########txt代表输出后缀名是txt的文件名#######")
    print("########脚本执行格式如下:####################")
    print("########python xxx.py txt###################")
    print("############################################")
    exit()
#获取后缀输入
suf = sys.argv[1]

#先清空文件
f = open("yuntiqu.log", "w")
f.truncate()
f.close()

for item in list_any:
    #print(item)
    acc_suffix(item,suf)
