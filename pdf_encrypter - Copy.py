import os, argparse, PyPDF2
parser = argparse.ArgumentParser()
parser.add_argument('password')
arg = parser.parse_args()
for i, j, k in os.walk('.'):
    for l in k:
        if l.endswith('.pdf'):
            reading_file = open(i + '\\\\' + l, 'rb')
            reader = PyPDF2.PdfReader(reading_file)
            if reader.is_encrypted == False:
                writer = PyPDF2.PdfWriter()
                pages = reader.pages
                for page in pages:
                    writer.add_page(page)
                writer.encrypt(arg.password)
                file = l.split('.pdf')[0]
                writing_file = open(f'{file}_encrypted.pdf', 'wb')
                writer.write(writing_file)
                reading_file.close()
                writing_file.close()

