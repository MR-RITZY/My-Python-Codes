import pyperclip,re
text = pyperclip.paste()
textPattern = re.compile(r'\n')
text = '*' + textPattern.sub(r'\n*', text)
pyperclip.copy(text)
