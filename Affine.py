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

def Encrypt(message):
    cipher=''
    for letter in message:
        if letter==' ':
            cipher+=' '
        else:
            x=(key1*list1[letter]+key2)%26
            cipher+=list2[x]
    return cipher

def Decrypt(cipher):
    message=''
    inverse=0
    flag=0
    for i in range(26):
      flag= (key1*i)%26
      if flag==1:
          inverse=i
          break
    for letter in cipher:
        if letter==' ':
            message+=' '
        else:
            x=(inverse*(list1[letter]-key2))%26
            message+=list2[x]
    return message

print(" \n \t \t \t AFFINE CIPHER ")

key1=int(input(" \n\t Enter 1st Key : "))
key2=int(input(" \t Enter 2nd Key : "))
message=input(" \n\t Enter message ")
message=message.upper()
print()
print(" \t\t Message : ",message)

ciphertext=Encrypt(message)
print(" \t\t Encrypted Text : " + ciphertext)

plaintext=Decrypt(ciphertext)
print(" \t\t Decrypted Text : " + plaintext)
