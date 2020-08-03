#python3
#PyandExcel.py

import openpyxl, pprint


print('Opening Student.xlsx...\n')
wb = openpyxl.load_workbook('Students.xlsx')

sheet = wb['Student Data']
studentsData = { }

print('Reading Rows\n')
