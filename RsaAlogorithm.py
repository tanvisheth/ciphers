import random

def check_prime(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(a, b):
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a  
    ob = b 
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob 
    if ly < 0:
        ly += oa  
    return lx

def get_mod_expo(base, exponent, modulus):
    result = 1
    while exponent:
        exponent, d = exponent // 2, exponent % 2
        if d:
            result = result * base % modulus
        base = base * base % modulus
    return result


def generate_keypair(p, q):
    if not (check_prime(p) and check_prime(q)):
        raise ValueError(' \n\t\t\t Both numbers must be prime.')
    elif p == q:
        raise ValueError(' \n\t\t\t p and q cannot be equal!')
   
    n = p * q
    print(" \n\t\t\t Value of n (where, n = p * q) is: ", n)

    phi = (p-1)*(q-1)
    print(" \n\t\t\t Value of phi(n) (where, phi(n) = (p-1)*(q-1)) is: ", phi)

    #e = random.randrange(1, phi)
    print(" \n\t\t Enter e such that is co-prime to ", phi, ": ",end=" ")
    e = int(input())
    g = gcd(e, phi)
    if g != 1:
        print(" \n\t\t The number you entered is not co-prime ")
        e = int(input())
    print("\n\t\t Value of e entered is: ", e)
    d = multiplicative_inverse(e, phi)
    print(" \n\t\t\t The value of d is:",d)
    return (e, n), (d, n)

def encrypt(public_key, to_encrypt):
    key, n = public_key
    cipher = get_mod_expo(to_encrypt, key, n)

    return cipher


def decrypt(private_key, to_decrypt):

    key, n = private_key
    decrypted = get_mod_expo(to_decrypt, key, n)
    return decrypted

print(" \n \t \t \t \t RSA ALGORITHM ")
p = int(input(" \n\t\t Enter a prime number for p: "))
q = int(input(" \t\t Enter a prime number for q: "))
print(" \n\t\t Prime numbers entered, p: ", p, " and q: ", q)

print("\n\t\t Generating Public/Private key-pairs!")
public, private = generate_keypair(p, q)
print(" \n\t\t\t Private Key is:",private)
print(" \n\t\t\t Public Key is:",public)

message = int(input(" \n\t\t Enter Message "))
print(" \n\t\t\t Your message is:",message)

encrypted_msg = encrypt(public, message)
print(" \n\t\t\t Encrypted message is:", encrypted_msg)

decrypted_msg = decrypt(private, encrypted_msg)
print(" \n\t\t\t Decrypted message is:", message)

