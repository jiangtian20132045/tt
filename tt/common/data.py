#coding:utf-8
import xlrd,xlwt
#打开表格

class ExcelUnit():
    def __init__(self,excelpath,sheetname):
        self.data = xlrd.open_workbook(excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        #获取第一行作为key值
        self.key = self.table.row_values(0)
        #获取总行数
        self.rowNum = self.table.nrows
        #获取总列数
        self.colNum = self.table.ncols

    def dict_Data(self):
        if self.rowNum <=1:
            print("总行数小于1")
        else:
            r = []
            j =1
            for i in range(self.rowNum-1):
                s ={}
                #从第二行获取对应的值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.key[x]] = values[x]
                r.append(s)
                print(r)
                j+=1
            return r

if __name__ == "__main__":
    print("c")
    filepath = "test.xlsx"
    sheetname = "Sheet1"
    print("b")
    data = ExcelUnit(filepath,sheetname)
    print("a")
    print(data.dict_Data())



