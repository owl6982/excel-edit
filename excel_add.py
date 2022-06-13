import xlrd,xlwt
from xlutils.copy import copy
from tkinter import INSERT
import os
import chardet
import re
import time
import operator
def read_content(content_file1,content_file2,content_name1,content_name2):
    data1 = []
    data2 = []
    name1 = content_name1
    name2 = content_name2

    print("正在读取文件...")
    data_xsls1 = xlrd.open_workbook(content_file1)


    sheet_name1 = data_xsls1.sheets()[0]
    #print(sheet_name)
    sheet_name2 = data_xsls1.sheet_by_index(0)
    #print(sheet_name1)
    count_nrows1 = sheet_name1.nrows  #获取总行数
#    print(count_nrows)
    count_nocls1 = sheet_name1.ncols  #获得总列数
    line_value = sheet_name1.row_values(0)
    for i in range(0,count_nrows1):
        data_1 = {}
        for j in range(0,count_nocls1):
            data_1[line_value[j]]=sheet_name1.cell(i,j).value  #根据行数来取对应列的值，并添加到字典中
 #           print(data_1)
        data1.append(data_1)

    print("读取文件1完成")

    
       
    print("正在读取文件...")
#    data_xsls = xlrd.open_workbook(content_file2)
    data_xsls2 = xlrd.open_workbook(content_file2)
    sheet_name3 = data_xsls2.sheets()[0]
#    print(sheet_name)
    sheet_name4 = data_xsls2.sheet_by_index(0)
#    print(sheet_name1)
    count_nrows2 = sheet_name3.nrows  #获取总行数
#    print(count_nrows)
    count_nocls2 = sheet_name3.ncols  #获得总列数
    line_value = sheet_name3.row_values(0)
    for i in range(0,count_nrows2):
        data_2 = {}
        for j in range(0,count_nocls2):
            data_2[line_value[j]]=sheet_name3.cell(i,j).value  #根据行数来取对应列的值，并添加到字典中
#            print(data_1)
        data2.append(data_2)
    print(data2)
    print("读取文件2完成")

    list1 = data1[0] #列表的第一行提取
    list2 = data2[0]

    excel = copy(wb=data_xsls1) # 完成xlrd对象向xlwt对象转换
    excel_table = excel.get_sheet(0) # 获得要操作的页
    table = data_xsls1.sheets()[0]

    for l in range(1, count_nrows1):
        data1_list1 = data1[l]
        data1_list2 = list(list1.keys()) #获取key值
#        for m in range(0,count_nocls1 ):
#            if operator.eq(name2,data1_list2[m]):
#                break #获取所需项目在列表中的列数值
        for p in range(1, count_nrows2):
                data2_list1 = data2[p]
                str1 = str()
                str2 = str()
                str1 = data1_list1[name1]
                str2 = data2_list1[name1]
            
                if operator.eq(str1,str2):
                    print(operator.eq(str1,str2))
                    excel_table.write(l,count_nocls1+1,data2_list1[name2])
                    excel_table.write(0,count_nocls1+1,name2)
                    excel.save(content_file1)

    
    
