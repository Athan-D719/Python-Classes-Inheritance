import os
import glob

path = "C:/Users/Asus/Desktop/bot"'
text_files = glob.glob(path + "/**/*.txt", recursive = True)
print(text_files)

for i in text_files[0]:
    a += 1
    if 's' in i:
        l.append(a)
print(l)
text = re.findall("bot([^/S]*)", text_files[0])
print(text[0][1:])

text = text_files[0].find('s')
print(text)
t2 = text_files[0][26:41]
print(t2)
#########################################################################
L = 'A line of text.\n'.rstrip() #NO SPACING
print(L)

print('Hello, ' + os.getlogin() + '! How are you?') #LOGGED IN

print('hello', 'world', sep='\n') #SEPARATION