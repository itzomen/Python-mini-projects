#python3
#PyandExcel.py
#install openpyxl
import openpyxl, re


# Registration Number Regex
regNoRegex = re.compile(r'''(
    ([F][E])  #Faculty
    (\d{2})      #Year registered
    ([ABC])        #Category
    (\d{3})      #Number
    )''',  re.VERBOSE)
    
def GetExcelData( ):
	#Reads and creates list of data from two columns of excel file
	#col1 column having regNo in excel
	#col2 column having name in excel
	print('Preparing to read name and associated regular pattern')
	
	excel = input('Enter the name of the excel file: ')
	col1 = input('Enter Column letter with regNo: ')
	col2 = input('Enter Column letter with name: ')
	
	print('Opening '+ excel + '.xlsx...\n')
	wb = openpyxl.load_workbook(excel +'.xlsx')
	sheet = wb.active
	print('Adding Data to '+ excel +' list\n')
	excel = [ ]
	for row in range(2, sheet.max_row + 1):
		regNo = sheet[col1 + str(row)].value
		studentName = sheet[col2 + str(row)].value
		if regNoRegex.match(regNo):
			excel.append( [studentName, regNo ])
	
	print('Data extracted Successfully\n')
	return excel

#excel name Students
#columns AB
studentsData = [ ]
studentsData = GetExcelData( )
#excel name Form	
#columns CB
formData = [ ]
formData = GetExcelData( )

#Verifing form infos
print('Fake Entries')
for i in formData:
		if i not in studentsData:
			print(i)
print('Duplicates')
#printing out duplicates
for x in formData:
		if formData.count(x)>1:
			print(x)				
