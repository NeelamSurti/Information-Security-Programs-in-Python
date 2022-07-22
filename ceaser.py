# Ceaser Cipher Encryption Decryption and Crypt Analysis
plaintext = input("Enter the value of Plaintext : ")
key = int(input("Enter the value of key : "))

def encrypt(p,k):
    cipher=""
    for i in p:
        cipher += chr((((ord(i)+k)-97)% 26)+97)
    return cipher
    
ciphertext = encrypt(plaintext,key)
print("Ciphertext for the plain text :",plaintext," is ",ciphertext)

def decrypt(c,k):
    plain=""
    for i in c:
        plain += chr((((ord(i)-k)-97)% 26)+97)
    return plain

decrypted_plain = decrypt(ciphertext,key)
print("Plaintext for the cipher text :",ciphertext," is ",decrypted_plain)

def crypt_analysis(c,p):
    for j in range(1,26):
        plain=""
        for i in c:
            plain += chr((((ord(i)-j)-97)% 26)+97)
        if(plain == p):
            break
    return j
    
k = crypt_analysis(ciphertext,plaintext)
print("Key after crypt_analysis : ",k)

