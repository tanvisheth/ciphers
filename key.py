def encrypt():
    strr=input("\n\t Enter the string : ")
    str1=""
    str2=""
    for i in range(len(strr)):
      if i%2==0:
        str1+=strr[i]
      else:
        str2+=strr[i]
    print(" \n\t\t Encrypted Text : ",str1+str2)

def decrypt():
    strr=input(" \n\t Enter the string : ")
    str1=""
    if len(strr)%2 != 0:
      strr=strr+'$';
    a=0
    while(a < len(strr)/2):
      str1=str1+strr[a]
      str1=str1+strr[a+int(len(strr)/2)]
      a+=1
    print(" \n\t\t Decryption Text : ",str1.replace('$',''))

print(" \n \t \t \t KEYLESS TRANPOSITION CIPHER ")
while True:
    choose = input(" \n\t Type '1' for encryption and '2' for decrytion ")
    if(choose=='1'):
        encrypt()
    elif(choose=='2'):
        decrypt()
    else:
        print(" \n\t\t You entered the wrong option. ")
    c=input(" \n\t Do you want to continue ")
    if c.lower()!="y":
        break
