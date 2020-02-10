# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 上午9:59
# @Author  : Hui
# @File    : readExecl.py

import os
import xlrd
excel_path = os.path.abspath("../dataList/excelCase.xlsx")
class ReadExcel():

    def readExcel(self,fileName=excel_path, SheetName="Sheet1"):#获取sheet*表格

        data = xlrd.open_workbook(fileName)
        ##通过名称获取路径下的表格名称
        table = data.sheet_by_name(SheetName)

        nrows = table.nrows
        ncols = table.ncols

        if nrows > 1:
            # 获取第一列的内容，列表格式:0代表第一行，依次类推
            keys = table.row_values(0)
            listApiData = []
            # 获取每一行的内容，列表格式
            for col in range(1, nrows):#根据索引从第二行开始取，直到去完所有的行
                values = table.row_values(col)#打印每一行的内容

                # keys，values这两个列表一一对应来组合转换为字典
                #先用zip() 函数可以对具有相同数量的元素的序列进行配对，然后根据dict()方法形成字典
                api_dict = dict(zip(keys, values))
                listApiData.append(api_dict)

            return listApiData
        else:
            print("表格未填写数据")

if __name__ == '__main__':
    t = ReadExcel()
    # excel_path = os.path.abspath("../dataList/excelCase.xlsx")  # 获取文件路径
    # t.readExcel(excel_path, "Sheet1")

    t.readExcel()