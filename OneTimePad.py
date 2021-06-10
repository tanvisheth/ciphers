import random

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def encrypt(plaintext):
    otp = "".join(random.sample(charset, len(charset)))
    result = ""

    for c in plaintext.upper():
        if c==' ':
            result=result+c
        if c not in otp:
            continue
        else:
            result += otp[charset.find(c)]

    return otp, result

def decrypt(otp, secret):
    result = ""

    for c in secret.upper():
        if c==' ':
            result=result+c
        if c not in otp:
            continue
        else:
            result += charset[otp.find(c)]
    return result


print(" \n \t \t \t ONE TIME PAD CIPHER ")
vector = input(" \n Enter Vector ")
encrypted = encrypt(vector)
decrypted = decrypt(encrypted[0], encrypted[1])


print(" \n\t Test Vector: " + vector)
print(" \t OTP: " + encrypted[0])
print(" \t Encrypted: " + encrypted[1])
print(" \t Decrypted: " + decrypted)


