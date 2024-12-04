import openpyxl, csv
from pathlib import Path
Path('excel_csv').mkdir(exist_ok = True)
for file in list(Path('.').glob('*.xlsx')):
    excelist = []
    excel = openpyxl.load_workbook(file)
    for sheetname in excel.sheetnames:
        sheet = excel[sheetname]
        rows = list(sheet.rows)
        for row in rows:
            rowdata = []
            for cell in row:
                rowdata.append(cell.value)
            excelist.append(rowdata)
        with open((Path('excel_csv') / f"{Path(file).stem}_{sheetname}_.csv"),
        'w', newline = '') as writefile:
            writer = csv.writer(writefile, delimiter = '\t', lineterminator = '\n\n')
            for rowdata in excelist:
                writer.writerow(rowdata)
