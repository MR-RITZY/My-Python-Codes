def clearup(text, clear):
    import re
    clas = ''
    for i in clear:
        clas = clas +'[' + clear + ']'
    if clear == '':
        clearbegin = re.compile(r'^\s*')
        clearend = re.compile(r'\s*$')
    else:
        clearbegin = re.compile(r'^%s*' %(clas))
        text = clearbegin.sub('',text)
        clearend = re.compile(r'%s*$' %(clas))
        text = clearend.sub('',text)
    text = clearbegin.sub('', text)
    text = clearend.sub('', text)
    print(text)

