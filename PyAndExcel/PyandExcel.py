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
maxStudent = sheet.max_row

print('Reading Rows\n')
for row in range(2, maxStudent + 1):
	regNo = sheet['A' + str(row)].value
	studentName = sheet['B' + str(row)].value
	studentsData.append( [studentName, regNo ])



print('Opening Form.xlsx...\n')
wb = openpyxl.load_workbook('Form.xlsx')
#opening the sheet having the filled infos
sheet1 = wb['Sheet1']

print('Verying entry Rows\n')
for row in range(2, sheet1.max_row + 1):
	reg = sheet1['C' + str(row)].value
	name = sheet1['B' + str(row)].value
	
	if regNoRegex.match(reg):
		pass
	else:
		print('Invalid RegNo row:'+ str(row))
		
	for i in range(0, maxStudent):
		for k in range(1,5):
			if reg == studentsData[i][-k]
			
		if reg in studentsData[i][2]:
			pass
		else:
			print()
