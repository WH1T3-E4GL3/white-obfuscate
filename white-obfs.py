import os
import marshal
import logging


yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
red = '\033[91m'
os.system("clear")
banner = yellow+"""
\t
+-------------------------------------------------------------------+
│                                                                   │
│  █ █ █ █▄█ ▀█▀ ▀█▀ █▀▀   █▀█ █▄▄ █▀▀ █ █ █▀▀ █▀▀ ▄▀▄ ▀█▀ █▀▀      │
│  ▀▄▀▄▀ █ █ ▄█▄  █  ██▄   █▄█ █▄█ █▀  █▄█ ▄██ █▄▄ █▀█  █  ██▄      │
│                                                                   │
│ 𝗔𝘂𝘁𝗵𝗼𝗿 : 𝘄𝗵𝗶𝘁𝗲 𝗲𝗮𝗴𝗹𝗲       𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 : 𝗵𝘁𝘁𝗽𝘀://𝘁.𝗺𝗲/𝗞𝗮_𝗞𝘀𝗛𝗶_𝗛𝗮𝗧𝗮𝗞𝗲
│                                                                   │
+-------------------------------------------------------------------+
			white obfuscate

\n"""+clear

print(banner)


def mode1(files, string):
    s = open(files).read()
    z = []
    for i in s:
        z.append(ord(i))
    pea = []
    for i in z:
        pea.append(string.replace("'", "").replace('"', '')*i)
    file = """
# coding=utf-8
# obfuscated with white obfuscate : https://github.com/WH1T3-E4GL3/white-obfuscate

d={};exec("".join([chr(len(i)) for i in d]))
    """.format(pea)
    open(files.replace(".py", "encrypted.py"), "w").write(file)
    logging.info(" saved as "+files.replace(".py", "encrypted.py"))
    print("File encrypted successfully as '{}'".format(
        files.replace(".py", "encrypted.py")))


def mode2(file):
    x = open(file).read()
    m = compile(x, '', 'exec')
    k = marshal.dumps(m)
    l = open('encoded-'+file, 'w')
    l.write('import marshal\n')
    l.write('exec(marshal.loads('+repr(k)+"))")
    l.close()
    print('File encoded successfully as \'encoded-{}\''.format(file))


while True:
    print(lgreen+"""
+-------------------------------------------------------------------+
│                                                                   │
│               1. Mode-1 (string substitution)                     │
│                                                                   │
│               2. Mode-2 (marshall encoding)                       │
│                                                                   │
│               3. Exit                                             │
│                                                                   │
+-------------------------------------------------------------------+
 """+clear)
    number = int(input("Enter the number you want from above > "))

    if number == 1:
        file = input("Enter the name of the file to be encrypted: ")
        string = input("Enter the string to be used for substitution cipher: ")
        mode1(file, string)

    elif number == 2:
        file = input("Enter the name of the file to be encoded: ")
        mode2(file)

    elif number == 3:
        break

    else:
        print(red + "[ERROR!]" + clear + " Invalid input, please try again.")

