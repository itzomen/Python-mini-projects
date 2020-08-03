#PyandExcel.py

import openpyxl, pprint


print('Opening Student.xlsx...')
book1 = openpyxl.load_workbook('Students.xlsx')

sheet1 = book1.get_sheet_by_name('Student Data')



print('Opening Form_info.xlsx...')
book2 = openpyxl.load_workbook('Form_info.xlsx')

