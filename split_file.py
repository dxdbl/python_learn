# coding:utf-8
####################################################
# 程序功能 : 根据文件行数生成新的文件
# 程序运行说明 : python split_line.py file 1000
# 作者 : mhf @ 2018-02-08 16:39
# 版本 : V1.0
# 修改时间 : 2018-03-28
# 修改人 : mahf
# 修改说明 : 解决中文编码错误问题
####################################################
import sys

def se_file_by_line(filename,line_num):
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
            f = open(file_head + "-" + str(findex) + ".txt", "w",encoding='utf-8')
            findex += 1
        counter += 1
        f.write(line)
        if counter%line_num == 0 and counter != file_count:
            f.close()
            f = open(file_head + "-" + str(findex) + ".txt", "w",encoding='utf-8')
            findex += 1
    f.close()

#脚本执行
#判断传入参数个数
if len(sys.argv) != 3:
    print("error!" + "\n" + "格式如下:python split_file.py filename 1000")
    print("其中filename是需要分割的文件名" + "\n" + "1000是每隔多少行分割!")
    exit()
# 传参数
filename = sys.argv[1]
lines = sys.argv[2]
try:
    se_file_by_line(filename,int(lines))
    print("生成文件成功,请查看文件目录!")
except:
    print("出现意外,程序结束,请检查输入时候正确!")
