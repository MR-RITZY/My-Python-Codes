def pigLatin(translate):
    convert = translate.split(' ')
    print(convert)
    for i, j in enumerate(convert):
        if i == len(convert)-1:
            first,second,third = j.partition('.')
            j = first
        if str(j[0]).isdecimal():
            convert[i] = j
        elif j.startswith('a') or j.startswith('A') or j.startswith('E') or j.startswith('e') or j.startswith('i') or j.startswith('I') \
        or j.startswith('O') or j.startswith('o') or j.startswith('u') or j.startswith('U') or j.startswith('Y') or j.startswith('y'):
            convert[i] = j + 'yay'
            if j.isupper():
                convert[i] = convert[i].upper()
            elif j.islower():
                convert[i] = convert[i].lower()
            else:
                convert[i] = convert[i].title()
        elif j[1] != 'a' and  j[1] != 'A' and  j[1] != 'E' and  j[1] != 'e' and  j[1] !='i' and  j[1] !='I' and  j[1] !='O' and  j[1] !='o' \
            and  j[1] != 'u' and  j[1] != 'U' and j[1] != 'y' and  j[1] != 'Y':
            first,second,third = j.partition(j[0]+j[1])
            convert[i] = first + third + second + 'ay'
            if j.isupper():
                convert[i] = convert[i].upper()
            elif j.islower():
                convert[i] = convert[i].lower()
            else:
                convert[i] = convert[i].title()
        else:
            first,second,third = j.partition(j[0])
            convert[i] = first + third + second + 'ay'
            if j.isupper():
                convert[i] = convert[i].upper()
            elif j.islower():
                convert[i] = convert[i].lower()
            else:
                convert[i] = convert[i].title()
    translation = ' '.join(convert)
    translation = translation + '.'
    print(translation)
pigLatin('My name is AL SWEIGART and I am 4,000 years old.')
