import argparse, ezsheets
parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('ext')
arg = parser.parse_args()
ssheet = ezsheets.upload(arg.filename)
if arg.ext == 'xlsx':
    ssheet.downloadAsExcel(f'downloaded_{arg.filename}.{ext}')
elif arg.ext == 'pdf':
    ssheet.downloadAsPDF(f'downloaded_{arg.filename}.pdf')
elif arg.ext == ''
