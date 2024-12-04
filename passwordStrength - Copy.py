def passwordStrength():
    import re
    password = input('Set your password\n')
    uppercase = re.compile(r'[A-Z]')
    checkUp = uppercase.search(password)
    lowercase = re.compile(r'[a-z]')
    checkLow = lowercase.search(password)
    digit = re.compile(r'\d')
    checkDigit = digit.search(password)
    while True:
        if checkUp == None or checkLow == None or checkDigit == None or len(password) <= 8:
            print('Invalid! Password must have atleast one uppercase letter, one lowercase letter, a digit and must be 8 character long.')
            password = input('Set your password correctly as instructed.\n')
        break
    print('Password set!')

