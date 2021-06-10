import string
def encrypt(pt,key):
    cipher=""
    for c in pt:
        if c in string.ascii_lowercase:
            index=ord(c)-ord('a')
            cipher+=key[index]
        else:
            cipher+=c
    return cipher

def decrypt(ct,key):
    plain=""
    for c in ct:
        if c in string.ascii_lowercase:
            index=key.find(c)
            plain+=chr(index+ord('a'))
        else:
            plain+=c
    return plain

print(" \n \t \t \t MONOALPHABETIC CIPHER ")
pt = input(" \n Enter Message ")
key = input(" Enter Key ")

print()
print(" \t Message : " + pt)
print(" \t Key : " + key)

encrypted=encrypt(pt,key)
print(" \t Encrypted Text : " + encrypted)

decrpyted=decrypt(encrypted,key)
print(" \t Decrypted Text : " + decrpyted)


