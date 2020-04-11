import random
print('Input the text you want to translate',end=': ')
english = input()
morse = ''
for char in english:
    if char == ' ':
        morse+='//'
    elif char == '.':
        morse+='//\n'
    else:
        number = random.randint(1,3)
        for num in range(0,number):
            dotOrDash = random.randint(0,1)
            if dotOrDash == 0:
                morse+='•'
            else:
                morse+='-'
        morse+='/'
print('The morse code equivalent is:\n', morse)