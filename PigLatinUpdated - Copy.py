def transPigLatin(trans):
    trans = trans.split(' ')
    import re
    check_vowel, check_conso, check_digit = re.compile(r'^[aAeEiIoOuUyY]'), re.compile(r'[aAeEiIoOuUyY]'), re.compile(r'^\d')
    for i, j in enumerate(trans):
        if i == len(trans) - 1:
            first, second, third = j.partition('.')
            j = first
        if check_digit.search(j) != None:
            trans[i] = j
        elif check_vowel.search(j) != None:
            trans[i] = j + 'yay'
            if j.isupper():
                trans[i] = trans[i].upper()
            elif j.islower():
                trans[i] = trans[i].lower()
            else:
                trans[i] = trans[i].title()
        elif check_conso.search(j[1]) != None:
            first, second, third = j.partition(j[1])
            trans[i] = second + third + first + 'ay'
            if j.isupper():
                trans[i] = trans[i].upper()
            elif j.islower():
                trans[i] = trans[i].lower()
            else:
                trans[i] = trans[i].title()
        else:
            check = check_conso.search(j).group()
            first, second, third = j.partition(check)
            trans[i] = second + third + first + 'ay'
            if j.isupper():
                trans[i] = trans[i].upper()
            elif j.islower():
                trans[i] = trans[i].lower()
            else:
                trans[i] = trans[i].title()
    trans = ' '.join(trans)
    trans = trans + '.'
    print(trans)
transPigLatin('My name is AL SWEIGART and I am 4,000 years old.')






