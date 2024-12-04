import openpyxl, argparse
from pathlib import Path
parser = argparse.ArgumentParser()
parser.add_argument('spreadsheet')
parser.add_argument('--sheetname')
arg = parser.parse_args()
wbook = openpyxl.load_workbook(arg.spreadsheet)
if arg.sheetname is not None:
    sheet = wbook[arg.sheetname]
else:
    sheet = wbook.active
wcolumns = sheet.columns
for i in wcolumns:
    fil = open(f'{Path(arg.spreadsheet).stem}_{sheet.title}_{i[0].column}.txt', 'w')
    for j in i:
        fil.write(str(j.value) + '\n')
    fil.close()
