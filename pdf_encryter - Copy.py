import os, argparse, PyPDF2
parser = argparse.ArgumentParser()
parser.add_argument('password')
for i, j, k in os.walk('.'):
    for l in k:
        if l.endswith('.pdf'):
            reader = PyPDF2.PdfReader(open(l), 'rb')
            writer = PyPDF2.PdfWriter()
            pages = reader.pages
            for page in pages:
                writer.add_page(page)
            writer.encrypt(password)
            file = l.split('.pdf')[0]
            writer.write(open(f'{file}_encrypted.pdf'), 'wb')

