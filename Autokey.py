list1={'A':0,'B':1,'C': 2, 'D': 3, 'E': 4,
       'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
         'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
         'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
         'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

list2={0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
         5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
         10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
         15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
         20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

def generate_key(message,key):
    i=0
    while True:
        if len(key)==len(message):
            break
        if message[i]==' ':
            i+=1
        else:
            key+=message[i]
            i=i+1
    return key

def Encrypt(message,key2):
    cipher=''
    i=0
    for letter in message:
        if letter==' ':
            cipher+=' '
        else:
            x=(list1[letter]+list1[key2[i]])%26
            i=i+1
            cipher+=list2[x]
    return cipher

def Decrypt(cipher,key2):
    message=''
    i=0
    for letter in cipher:
        if letter==' ':
            message+=' '
        else:
            x=(list1[letter]-list1[key2[i]]+26)%26
            i=i+1
            message+=list2[x]
    return message

print(" \n \t \t \t AUTOKEY CIPHER ")

message=input(" \n Enter message ")
key=input(" \n Enter Secret Key : ")

message=message.upper()
key=key.upper()
key2=generate_key(message,key)
print()
print(" \t Message : ",message)
print(" \t Key : ",key)

ciphertext=Encrypt(message,key2)
print(" \t Encrypted Text : " + ciphertext)

plaintext=Decrypt(ciphertext,key2)
print(" \t Decrypted Text : " + plaintext)

