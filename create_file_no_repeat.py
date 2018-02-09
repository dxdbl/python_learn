# coding:utf-8
###################################################
# 创建文件时，先检查是否有同名文件（使用os.path.isfile）
# 如果有，则在文件名后加上编号n来创建。
# 1. 使用os.path.isfile判断文件是否存在
# 2. 使用递归函数判断
# 3. 添加编号时, 使用可变list 传值n=[0]
###################################################
import os

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
    print("创建文件 %s " % return_name + "成功!")
    return return_name
f = open(check_filename_available('test1.txt'),'w')
f.write('Checking func!')
f.close()
