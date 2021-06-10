import hashlib

print(" \n \t \t \t DIFFIE HELLMAN ALGORITHM ")
g=int(input(" \n\t Enter shared value (G) : "))
p=int(input(" \t Enter prime number (P) : "))

a=int(input(" \n\t Enter 1st private key (a) : "))
b=int(input(" \t Enter 2nd private key (b) : "))

A = (g**a) % p
B = (g**b) % p


print('\n\t G: ',g,' (a shared value), P: ',p, ' (a prime number)')

print('\n\t Alice calculates: ')
print(' \t\t a (Alice Private Key): ',a)
print(' \t\t Alice value (A): ',A,' (G^a) mod P')

print(' \n\t Bob calculates: ')
print(' \t\t b (Bob Private Key): ',b)
print(' \t\t Bob value (B): ',B,' (G^b) mod P')

print(' \n\t Alice calculates: ')
keyA=(B**a) % p
print(' \t\t Key: ',keyA,' (B^a) mod P')
print(' \t\t Key: ',hashlib.sha256(str(keyA).encode()).hexdigest())

print(' \n\t Bob calculates: ')
keyB=(A**b) % p
print(' \t\t Key: ',keyB,' (A^b) mod P')
print(' \t\t Key: ',hashlib.sha256(str(keyB).encode()).hexdigest())
