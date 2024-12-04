import re
isphone = re.compile(r'(\(\d\d\d\)) (\(\d\d\d\)) (\(\d\d\d\d\))')
phone = isphone.search('(415) (555) (4242)')
print(phone.group(3))
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers 11 pipers 10 lords 9 ladies 8 maids 7 swans 6 geese \
5 rings 4 birds 3 hens 2 doves 1 partridge'))

number = re.compile(r'(\d{1,3})((,\d\d\d)+)?')
a = '42'
b = '1,234'
c = '6,368,745'
e = '3'
d = '12,34,567'
s = '1234'

print((number.match(c)).group())
name = re.compile(r'[A-Z]\w+\sWatanabe')
l = name.match('Ha Watanabe')
print(l.group())

sen = re.compile(r'((Alice)|(Bob)|(Carol))\s((eats)|(pets)|(throws))\s((apples)|(cats)|(baseballs))\.', re.I)
sence = sen.match('BOB EATS CATS.')
print(sence.group())
