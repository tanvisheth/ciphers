import numpy as np
import math
np.keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)]
cipherMatrix = [[0] for i in range(3)]
plainMatrix = [[0] for i in range(3)]
np.inverseKeyMatrix = [[0] * 3 for i in range(3)]

def getKeyMatrix(key):
  k = 0
  for i in range(3):
    for j in range(3):
      np.keyMatrix[i][j] = ord(key[k]) % 65
      k += 1

def encrypt(messageVector):
  for i in range(3):
    for j in range(1):
      cipherMatrix[i][j] = 0
      for x in range(3):
        cipherMatrix[i][j] += (np.keyMatrix[i][x] * messageVector[x][j])
        cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipher1(message, key):
  getKeyMatrix(key)
  for i in range(3):
    messageVector[i][0] = ord(message[i]) % 65
  encrypt(messageVector)
  CipherText = []
  for i in range(3):
    CipherText.append(chr(cipherMatrix[i][0] + 65))
  print("\n\t\t Ciphertext: ", "".join(CipherText))

def getInverseKeyMatrix(key):
  getKeyMatrix(key)
  keyMatrix=np.keyMatrix
  from sympy import Matrix
  inverseKeyMatrix = Matrix(keyMatrix).inv_mod(26)
  np.inverseKeyMatrix = np.array(inverseKeyMatrix)

def HillCipher2(message, key):
  getInverseKeyMatrix(key)
  for i in range(3):
    messageVector[i][0] = ord(message[i]) % 65
  decrypt(messageVector)
  PlainText = []
  for i in range(3):
    PlainText.append(chr(int(round(plainMatrix[i][0]) + 65)))
  print("\n\t\t Plaintext: ", "".join(PlainText))

def decrypt(messageVector):
  for i in range(3):
    for j in range(1):
      plainMatrix[i][j] = 0
      for x in range(3):
        plainMatrix[i][j] = plainMatrix[i][j] % 26
        plainMatrix[i][j] += (np.inverseKeyMatrix[i][x] * messageVector[x][j])
      plainMatrix[i][j] = plainMatrix[i][j] % 26

while True:
    message = input(" \n\t Enter Message ")
    message = message.upper()
    key = input(" \n\t Enter Key ")
    print(" \n\t\t Your message is:",message)
    print(" \n\t\t Your key is:",key)
    key = key.upper()
    choose = input(" \n\t Type '1' for encryption and '2' for decrytion.")
    if(choose=='1'):
        HillCipher1(message,key)
    elif(choose=='2'):
        HillCipher2(message,key)
    else:
        print(" \n\t\t You entered the wrong option.")
    c=input(" \n\t Do you want to continue ")
    if c.lower()!="y":
        break
