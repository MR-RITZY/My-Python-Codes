TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
'busy': """Sorry, can we do this later this week or next week?""",
'upsell': """Would you consider making this a monthly donation?"""}

import sys, pyperclip

while len(sys.argv) < 2:

    keyphrase = input('Enter the keyphrase of message to be copied\n')

message = TEXT[keyphrase]

if message in TEXT:

    pyperclip.copy(message)

    pyperclip.paste()

else:

    message = input('No such keyphrase! write your message, get it copied\n')

    if message in list(TEXT.values()):

        ID = list(TEXTvalues()).index(message)

        print(f'The keyphrase for this message is  {(list(TEXT.keys()))[ID]}')

    pyperclip.copy(message)

    pyperclip.paste()



