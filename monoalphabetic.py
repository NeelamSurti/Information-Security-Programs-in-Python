plaintext=input("Enter the plaintext : ")
key="xyzabcdefghijklmnopqrstuvw"

def encrypt(plaintext,key):
    cipher=""
    for i in plaintext:
        if i.isupper():
            cipher += key[ord(i)-65]
        else:
            cipher += key[ord(i)-97]
    return cipher
 
ciphertext= encrypt(plaintext,key)
print("Plaintext is " + plaintext + " Ciphertext is " + ciphertext)

def decrypt(ciphertext,key):
    plain=""
    for i in ciphertext:
        #print(key.find(i))
        if i.isupper():
            plain += chr(key.find(i)+65)
        else:
            plain += chr(key.find(i)+97)
        
    return plain

plaintext= decrypt(ciphertext,key)
print("Ciphertext is " + ciphertext + " plaintext is " + plaintext)
