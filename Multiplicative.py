def encrypt(pttext,shift): 
    cipher = ''
    for i in range(len(pttext)):
        char=pttext[i]
        if char == ' ':
            cipher = cipher + char
        elif char.islower():
            cipher += chr(((ord(char) - 97)*shift) % 26 + 97)
        else: 
            cipher += chr(((ord(char) - 65)*shift) % 26 + 65)
    return cipher

def decrypt(cttext,shift): 
    plain = ''
    for i in range(len(cttext)):
        char=cttext[i]
        if char == ' ':
            plain = plain + char
        elif char.islower():
             plain += chr(int((ord(char) - 97)*shift) % 26 + 97)
        else: 
            plain += chr(int((ord(char) - 65)*shift) % 26 + 65)      
    return plain 

def inverse(a):
    a = a % 26
    for x in range(1, 26):
        if (a * x) % 26 == 1:
            return x
    return 1

print(" \n \t \t \t MULTIPLICATIVE CIPHER ")
plaintext = input(" \n Enter PlainText ")
shift = int(input(" Enter Number of Shift "))

print()
print(" \t Shift Number : " + str(shift))

encrypted=encrypt(plaintext,shift)
print(" \t Encrypted Text : " + encrypted)

decrpyted=decrypt(encrypted,inverse(shift))
print(" \t Decrypted Text : " + decrpyted)
