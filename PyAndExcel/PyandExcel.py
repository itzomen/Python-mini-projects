#python3
#PyandExcel.py

import openpyxl, pprint
#install openpyxl


print('Opening Student.xlsx...\n')
wb = openpyxl.load_workbook('Students.xlsx')
#opening the sheet having the data to be read
sheet = wb['Student Data']
studentsData = { }

print('Reading Rows\n')
for row in range(2, sheet.max_row + 1):
	regNo = sheet['A' + str(row)].value
	print(regNo +',' + str(sheet.max_row))

