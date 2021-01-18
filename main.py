import xlrd

ExcelSheet = "output.xls"


Book = xlrd.open_workbook(ExcelSheet)

first_sheet = Book.sheet_by_index(0)

print(first_sheet.row_values(0))

Headings = first_sheet.row_values(0)
Column2Heading = Headings[1]

print(Column2Heading)

i = 0
total = 0

for row in range(first_sheet.nrows):
    if str(first_sheet.cell(row,1).value) == "Pepsi":
        i = i + 1
        total = total + (first_sheet.cell(row,2).value)
    else:
        pass

print(i)
print(total)
print(total/i)



