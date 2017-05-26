import xlrd

workbook=xlrd.open_workbook('hi.xlsx')
print("there are{}sheets in the workbook".format(workbook.nsheets))
for booksheet in workbook.sheets():
    for col in range(booksheet.ncols):
        for row in range(booksheet.nrows):
            value=booksheet.cell(row,col).value
            print(value)