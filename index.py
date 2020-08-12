#===============================REGEX=======================
#Demo 1--------------
'''
import re;
regex1 = re.compile(r'anh (.*?) trai');
type(regex1);
chuoiDemo = "anh Phuc dep trai qua";
kq = regex1.search(chuoiDemo);

name = kq.group(1);

print(name)
'''
#Demo 2 ----------------
# import re
# noidung = '''
# 	nhat ky cua nang
# hom nay la ngay dep troi, mk gap anh Phuc rat la dep trai mk fall in love with him roi
# '''
# regex1 = re.compile(r'anh(.*?)rat'); #lay ket qua la tat ca
# kq = regex1.search(noidung);
# print(kq.group(1))

#Demo 3 --------------

# import re
# noidung = '''
# 	nhat ky cua nang
# hom nay la ngay dep troi, mk gap anh Phuc rat la dep trai mk fall in love with him roi
# sau do cuoi ngay mk lai gap dc anh Minh rat dep trai nua
# '''
# regex1 = re.compile(r'anh(.*?)rat');
# kq = regex1.findall(noidung);  #finall lay ket qua nam trong dau ngoac (.*?)
# print(kq) #=> list danh sach thoa man


#================================File=====================

import io
import os
from shutil import copyfile

#(os) get duong dan hien tai
# print(os.getcwd())

# (os) duong dan den thu muc
# os.chdir(r'C:\Users\Admin\OneDrive\Máy tính\Python-github\Python')

#(os) tao 1 file
# f = open('test.txt','w')
# f.close()

#(os) doi ten file
# os.rename('test.txt','new name.txt')

# (os) xoa file
# os.remove('new name.txt')

#(os) copy file
# copyfile('test.txt','test2.txt')

# ham viet file ko utf8
# def writeFileLine(filename, nd_line):
#     f = open(filename,"a")
#     f.write(nd_file + '\n')
#     f.close()

# ham viet file co utf8
# def writeUtf8(filename, nd_line):
#     f = open(filename, mode="a", encoding="utf-8") # chu a( mode ="a") la append
#     f.write(nd_line + '\n')
#     f.close()
    
# filename = 'test.txt'
# nd_line = 'anh Phúc đẹp trai'
# writeUtf8(filename, nd_line)

#(os) doc file
# f = io.open("test.txt", mode="r", encoding="utf-8")
# list_lines = f.readline()
# # print(list_lines)
# for line in list_lines:
#     print(line)


