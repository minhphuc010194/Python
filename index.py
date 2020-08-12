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
print(os.getcwd())