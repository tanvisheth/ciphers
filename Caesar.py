def encrypt(pttext,shift): 
    cipher = ''
    for char in pttext:
        if char == ' ':
            cipher = cipher + char
        elif char.islower():
            cipher += chr((ord(char) + shift - 97) % 26 + 97)
        else: 
            cipher += chr((ord(char) + shift - 65) % 26 + 65)
    return cipher 

def decrypt(cttext,shift): 
    plain = ''
    for char in cttext:
        if char == ' ':
            plain = plain + char
        elif char.islower():
             plain += chr((ord(char) - shift - 97) % 26 + 97)
        else: 
            plain += chr((ord(char) - shift-65) % 26 + 65)      
    return plain 


print(" \n \t \t \t ADDITIVE / CEASER CIPHER ")
plaintext = input(" \n\t Enter PlainText ")
shift = int(input(" \t Enter Number of Shift "))

print()
print(" \t\t Shift Number : " + str(shift))

encrypted=encrypt(plaintext,shift)
print(" \t\t Encrypted Text : " + encrypted)

decrpyted=decrypt(encrypted,shift)
print(" \t\t Decrypted Text : " + decrpyted)

