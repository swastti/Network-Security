def encrypted(string,shift):
            cipher=''
            for char in string:
                if char=='':
                    cipher=cipher+char
                elif char.isupper():
                    cipher=cipher+chr((ord(char)+shift-65)%26+65)
                else:
                    cipher=cipher+chr((ord(char)+shift-97)%26+97)
            return cipher

def dencrypted(string,shift):
            cipher=''
            for char in string:
                if char=='':
                    cipher=cipher+char
                elif char.isupper():
                    cipher=cipher+chr((ord(char)-shift-65)%26+65)
                else:
                    cipher=cipher+chr((ord(char)-shift-97)%26+97)
            return cipher

while True:
    op=int(input("\nChoose:\n1.Encryption\n2.Decryption\n3.Exit\n"))

    if op==1:
        text=input("Enter Text You Want to Encrypt:")
        s=int(input("Enter the key:"))
        print("The original String is: ",text)
        print("The Encrypted msg is: ",encrypted(text,s))
        
    elif op==2:
        etext=input("Enter Encrypted Text:")
        s=int(input("Enter the key:"))
        print("The Encrypted String is: ",etext)
        print("The decrypted msg is: ",dencrypted(etext,s))
        
    elif op==3:
        break

    else:
        print("Incorrect Option.Choose Again")