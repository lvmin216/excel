import xlrd

fileOutput = open('hi.txt','w')

# 可以在这里写一些固定的注释代码之类的
writeData = "-- @author:time\n\n\n"

workbook = xlrd.open_workbook('hi.xlsx')
print("There are {} sheets in the workbook".format(workbook.nsheets))


for booksheet in workbook.sheets():
    for col in range(booksheet.ncols):
        for row in range(booksheet.nrows):
            value = booksheet.cell(row, col).value
            if row == 0:
                writeData = writeData + '\t' + '["' + value + '"]' + ' = ' + '{ '
            else:
                writeData = writeData + '"' + str(booksheet.cell(row, col).value) + '" , '
        else:
            writeData = writeData + '} ,\n'
    else:
        writeData = writeData + '}\n\n'
else:
    fileOutput.write(writeData)

fileOutput.close()