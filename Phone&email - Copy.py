import pyperclip,re
text = pyperclip.paste()
phone = re.compile(r'(\(?\d{3})?(\s|-|\.\)?)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)(d{2,5}))?')
mail = re.compile(r'\w+@\w+\.com')
phone_number = phone.findall(text)
email = mail.findall(text)
contact = phone_number + email
contact = '\n'.join(contact)
if contact == '':
    print('No phone number or e-mail found')
else:
    pyperclip.copy(contact)

