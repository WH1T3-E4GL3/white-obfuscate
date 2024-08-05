import os
import marshal
import logging

# ANSI color codes
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
red = '\033[91m'

# Clear the terminal and display the banner
os.system("clear")
banner = yellow + """
\t
+-------------------------------------------------------------------+
│                                                                   │
│  █ █ █ █▄█ ▀█▀ ▀█▀ █▀▀   █▀█ █▄▄ █▀▀ █ █ █▀▀ █▀▀ ▄▀▄ ▀█▀ █▀▀      │
│  ▀▄▀▄▀ █ █ ▄█▄  █  ██▄   █▄█ █▄█ █▀  █▄█ ▄██ █▄▄ █▀█  █  ██▄      │
│                                                                   │
│ Author : whxite       Instagram : @whxitte
│                                                                   │
+-------------------------------------------------------------------+
\t\twhite obfuscate

""" + clear

print(banner)

def mode1(files, string):
    try:
        with open(files, 'r') as f:
            s = f.read()
        z = [ord(i) for i in s]
        pea = [string.replace("'", "").replace('"', '') * i for i in z]
        obfuscated_code = """
# coding=utf-8
# obfuscated with white obfuscate : https://github.com/WH1T3-E4GL3/white-obfuscate

d={};exec("".join([chr(len(i)) for i in d]))
        """.format(pea)
        with open(files.replace(".py", "encrypted.py"), "w") as f:
            f.write(obfuscated_code)
        logging.info("Saved as " + files.replace(".py", "encrypted.py"))
        print("File encrypted successfully as '{}'".format(files.replace(".py", "encrypted.py")))
    except Exception as e:
        print(red + "[ERROR]" + clear + " An error occurred: {}".format(e))

def mode2(file):
    try:
        with open(file, 'r') as f:
            x = f.read()
        m = compile(x, '', 'exec')
        k = marshal.dumps(m)
        encoded_filename = 'encoded-' + file
        with open(encoded_filename, 'w') as l:
            l.write('import marshal\n')
            l.write('exec(marshal.loads(' + repr(k) + "))")
        print("File encoded successfully as '{}'".format(encoded_filename))
    except Exception as e:
        print(red + "[ERROR]" + clear + " An error occurred: {}".format(e))

def main_menu():
    while True:
        print(lgreen + """
+-------------------------------------------------------------------+
│                                                                   │
│               1. Mode-1 (string substitution)                     │
│                                                                   │
│               2. Mode-2 (marshal encoding)                        │
│                                                                   │
│               3. Exit                                             │
│                                                                   │
+-------------------------------------------------------------------+
""" + clear)
        try:
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
                print(red + "[ERROR]" + clear + " Invalid input, please try again.")
        except ValueError:
            print(red + "[ERROR]" + clear + " Please enter a valid number.")

if __name__ == "__main__":
    main_menu()
