import pyperclip
text = pyperclip.paste()
lines = text.split('\n')
for i, j in enumerate(lines):
    lines[i] = '*' + j
text = '\n'.join(lines)
pyperclip.copy(text)
