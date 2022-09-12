def decrypted(string):
     for s in range(1,27):
            cipher=''
            for char in string:
                if char=='':
                    cipher=cipher+char
                elif char.isupper():
                    cipher=cipher+chr((ord(char)-s-65)%26+65)
                else:
                    cipher=cipher+chr((ord(char)-s-97)%26+97)
            print("Decrypted text :",cipher,"for the key:",s)

etext=input("Enter Encrypted Text:")
decrypted(etext)