#-*- coding:utf-8 -*-
######################################################
# 程序功能 :合并目录下的txt文档内容到一个文件
# 程序运行说明 :
# 作者 : mhf @ 2018-03-26
# 版本 : V1.0
# 修改时间 :
# 修改人 :
#######################################################
import os


#列出目录下的文件函数
def file_name(file_dir):
    for root , dirs , files in os.walk(file_dir):
        #print(root)    #当前目录路径
        #print(dirs)    #当前路径下所有子目录
        return files    #当前路径下所有非目录子文件

file_name_list = file_name("./before")
print("文件列表:" + str(file_name_list))

#打开文件等待写入结果
f = open("merge_files_result.txt","w",encoding='utf-8')

#循环读取文件夹下面的文档(不区分是否为txt)
print("读取每个文件的内容并写入目标文件:")
for i in file_name_list:
    print("---" + i + "---")
    file_dir = "before/" + i
    for line in open(file_dir,"r",encoding='utf-8'):
        print(line)
        f.write(line.rstrip('\n') + "\n")
f.close()
