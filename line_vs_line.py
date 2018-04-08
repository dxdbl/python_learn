#-*- coding:utf-8 -*-

f = open("left_and_right.txt","w",encoding='utf-8')
filename1 = input("请输入文档1名称:\n")
#filename1 = "left.txt"
filename2 = input("请输入文档2名称:\n")
#filename2 = "right.txt"
with open(filename1, 'r',encoding='utf-8') as fp1, open(filename2, 'r',encoding='utf-8') as fp2:
    fp1_len = len(fp1.readlines())
    print(fp1_len)
    fp2_len = len(fp2.readlines())
    print(fp2_len)
if fp1_len >= fp2_len:
    with open(filename1, 'r', encoding='utf-8') as fp1, open(filename2, 'r', encoding='utf-8') as fp2:
        for i in fp1:
            j = fp2.readline()
            print(i, j)
            f.write(i.strip("\n") + "    " + j.rstrip("\n") + "\n")
else:
    with open(filename1, 'r', encoding='utf-8') as fp1, open(filename2, 'r', encoding='utf-8') as fp2:
        for i in fp2:
            j = fp1.readline()
            print(i, j)
            f.write(j.strip("\n") + "    " + i.rstrip("\n") + "\n")
f.close()
