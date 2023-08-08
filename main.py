import random
import ast
import pyfiglet
import os

def encryption_generator(fname):
    mkey = dict()
    def listtostr(s):
        str1 = ""
        for j in s:
            str1 += str(j)
        return str1 
    for i in range(0,10):
        a = random.sample(range(0,10),4)
        a = listtostr(a)
        mkey.update({f"{i}":a})
    print(mkey)
    with open(f"{fname}.txt","w") as f:
        f.write(str(mkey))
    os.rename(f"#YOUR_PATH\\{fname}.txt" , f"#YOUR_PATH\\key\\{fname}.txt" )

def encrypter(a,b):
         # a = input("enter a number to encrypt:- ")
         # b = input("enter your key file name:- ")
        str1 = ""
        with open(f"#YOUR_PATH\\key\\{b}.txt","r") as k:
            data = k.read()
        ans = dict(ast.literal_eval(data))
        for i in a:
            z = ans.get(i)
            str1 += z 
        return str1

def decrypter(emsg,kname):
    with open(f"#YOUR_PATH\\key\\{kname}.txt","r") as f:
        data = f.read()

    key = dict(ast.literal_eval(data))
    k = list(key.keys())
    v = list(key.values())
    ans = ""
    for i in range(0,int(len(emsg)/4)):
        if i == 0:
            q = 0
            w = 4
        else :
            q = w
            w = w + 4
        pos = v.index(emsg[q:w])
        ans += k[pos]
    return ans


t1 = pyfiglet.figlet_format("ENCRYPTION",font='drpepper')
t2 = pyfiglet.figlet_format("DECRYPTION",font='drpepper')
t3 = pyfiglet.figlet_format("ALGORITHM",font='drpepper')

print(f"{t1}\n{t2}\n{t3}")
print("Note:- \n this program is currently in developement stage \n hence can only take integer input \n and not words ")
print("-"*30)
print('[+] Press 1 to generate a key')
print('[+] Press 2 to encrypt with a key')
print('[+] Press 3 to decrypt with a key')
print("-"*30)
print('\n')
operation = input(" [+] ")

if(operation == '1'):
    fname = input("Enter the name of the file (as per yor wish) \n [+] ")
    encryption_generator(fname)
    print(f"Operation successfull your key is generated and its name is {fname}.txt")

elif(operation == '2'):
    a = input("Enter the number to encrypt \n [+] ")
    b = input("Enter the file name of key don`t add extension (.txt/.csv) \n [+] ")
    msg = encrypter(a,b)
    print(f"Your encrypted msg is \n [+] {msg}")

elif(operation == '3'):
    emsg = input("Enter the Encrypted message \n [+] ")
    kname = input("Enter the file name of decryptionkey don`t add extension (.txt/.csv) \n  [+] ")
    ans = decrypter(emsg,kname)
    print(f"Your msg is \n [+] {ans}")
else:
    print("You entered wrong operation please enter correct operation")
