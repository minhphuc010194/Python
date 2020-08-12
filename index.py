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


#================================Thao tac voi File=====================

# import io
# import os
# from shutil import copyfile

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


#================================Thao tac voi excel===============

import openpyxl



def get_value_excel(filename, cellname):
    wb = openpyxl.load_workbook(filename)
    Sheet1 = wb['Sheet1']
    wb.close()
    return Sheet1[cellname].value

def update_value_excel(filename, cellname, value):
    wb = openpyxl.load_workbook(filename)
    Sheet1 = wb['Sheet1']
    Sheet1[cellname].value = value
    wb.close()
    wb.save(filename)
# Demo1
# filename = 'file.xlsx'
# cellname = 'G6'
# bien_x = get_value_excel(filename, cellname)
# print('bien_x', bien_x)

# Demo2
# filename = 'file.xlsx'
# cellname = 'G6'
# new_value = 'new update'
# update_value_excel(filename, cellname, new_value)

#Demo3
# F6->F10
# G6->G10
col_name_acc="F"
col_name_pass="G"
filename = 'file.xlsx'
for i_row in range(7,18):
    cell_name_acc="%s%s"%(col_name_acc,i_row)
    cell_name_pass="%s%s"%(col_name_pass,i_row)
    
    account = get_value_excel(filename, cell_name_acc)
    password = get_value_excel(filename, cell_name_pass)
    print('current account', account)
    print('current password', password)

    #hamlogin(account, password)
    input('pause')

# https://www.youtube.com/watch?v=xYux4Voj37o&list=PLYi1bpA-AvSDnbqKpqwIOykX6WPnjAmNQ&index=5