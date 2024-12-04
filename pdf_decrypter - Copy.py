import os, PyPDF2, argparse
parser = argparse.ArgumentParser()
parser.add_argument('password')
arg = parser.parse_args()
for i, j, k in os.walk('.'):
    for l in k:
        if l.endswith('.pdf'):
            file = open(i + '/' + l, 'rb')
            reader = PyPDF2.PdfReader(file)
            if reader.is_encrypted:
                decryption = reader.decrypt(arg.password)
                if decryption in [1, 2]:
                    print(f'PDF Reader Object of {l} in {i} successfully Decrypted')
                else:
                    print(f'Wrong Password! Access Denied to PDF Reader Object of {l} in {i}')
            file.close()
