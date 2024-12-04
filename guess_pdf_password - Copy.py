import PyPDF2, cProfile
cProfile.run('''dictionary = open('./automate_online-materials/dictionary.txt')
words = dictionary.readlines()
file = open('guests_encrypted.pdf', 'rb')
cases = [str.lower, str.upper, str.title]
password_found = False
for word in words:
    for case in cases:
        file.seek(0)
        reader = PyPDF2.PdfReader(file)
        decryption = reader.decrypt(case(word).strip())
        if decryption in [1, 2]:
            print(f'Password Found: Reader Object Decrypted\n\
And the password is: {case(word).strip()}')
            password_found = True
            break
    if password_found:
        break
if not password_found:
    print('Password not Detected - Not in Dictionary -')
file.close()''')
