import os, PyPDF2
os.chdir(r'..\Desktop\Books\300L files\300L first semester\tme314')
files = []
writer = PyPDF2.PdfWriter()
for i in os.listdir('.'):
    if (i.endswith('.pdf') and i.startswith('TME')):
        files.append(i)
for i, j in enumerate(files):
    reader = PyPDF2.PdfReader(open(j, 'rb'))
    if i == 0:
        for k in range(len(reader.pages)):
            writer.add_page(reader.pages[k])
    else:
        for k in range(3, len(reader.pages)):
            writer.add_page(reader.pages[k])
writer.write(open('combined_pdf.pdf', 'wb'))
