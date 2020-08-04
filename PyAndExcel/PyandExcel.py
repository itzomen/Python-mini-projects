#python3
#PyandExcel.py
#install openpyxl
import openpyxl, pprint, re


# Registration Number Regex
regNoRegex = re.compile(r'''(
    ([F][E])  #Faculty
    (\d{2})      #Year registered
    ([ABC])        #Category
    (\d{3})      #Number
    )''',  re.VERBOSE)
    

print('Opening Student.xlsx...\n')
wb = openpyxl.load_workbook('Students.xlsx')
#opening the sheet having the data to be read
sheet = wb['Student Data']
studentsData = [ ]
maxStudent = sheet.max_row - 1

print('Adding Students Data\n')
for row in range(2, sheet.max_row + 1):
	regNo = sheet['A' + str(row)].value
	studentName = sheet['B' + str(row)].value
	studentsData.append( [studentName, regNo ])



print('Opening Form.xlsx...\n')
wb = openpyxl.load_workbook('Form.xlsx')
#opening the sheet having the filled infos
sheet1 = wb['Sheet1']
formData = [ ]
maxData = sheet1.max_row -1
#Adding Form data
for row in range(2, sheet1.max_row + 1):
	reg = sheet1['C' + str(row)].value
	name = sheet1['B' + str(row)].value
	
	if regNoRegex.match(reg):
		pass
	else:
		print('Invalid RegNo row:'+ str(row))
	
