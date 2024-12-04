import openpyxl, argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('--sheetname')
parser.add_argument('orientation', choices = ['row', 'column'])
parser.add_argument('position', type = int)
parser.add_argument('spacing', type = int)
arg = parser.parse_args()
workbook = openpyxl.load_workbook(arg.filename)
if arg.sheetname != None:
    worksheet = workbook[arg.sheetname]
else:
    worksheet = workbook.active
if arg.orientation == 'row':
    worksheet.insert_rows(arg.position, amount = arg.spacing)
elif arg.orientation == 'column':
    worksheet.insert_cols(arg.position, amount = arg.spacing)
workbook.save(f'Updated{arg.filename}.xlsx')
print(f'File now saved as Updated{arg.filename}')
