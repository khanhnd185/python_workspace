# pip install openpyxl
import openpyxl
import os
print(os.getcwd())
os.chdir(r'E:\python_workspace\02_automating_tasks\12_excel')
wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))
print(wb.get_sheet_names())
sheet = wb.get_sheet_by_name('Sheet3')
print(sheet)
print(type(sheet))
print(sheet.title)
activeSheet = wb.get_active_sheet()
print(activeSheet)
print(activeSheet['A1'])
print(activeSheet['A1'].value)
