import openpyxl, os
os.chdir('./automate_online-materials')
workbook = openpyxl.load_workbook('produceSales.xlsx')
sheet = workbook['Sheet']
for i in range(2, sheet.max_row + 1):
    if sheet['A' + str(i)].value == 'Celery':
        sheet['B' + str(i)].value = 1.19
    elif sheet['A' + str(i)].value == 'Garlic':
        sheet['B' + str(i)].value = 3.07
    elif sheet['A' + str(i)].value == 'Lemon':
        sheet['B' + str(i)].value = 1.27
workbook.save('updatedProduceSales.xlsx')
