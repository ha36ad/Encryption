from stegano import lsb, lsbset
from stegano.lsbset import generators
import os
from cryptography.fernet import Fernet
        
#ask the user for the message that is encrypted
message = input("Write your message: ")

#encoding the message using AES
#generating the key for AES
def key_writing():
    k = Fernet.generate_key()
    with open("key.key","w+b") as file_k:
        file_k.write(k)
        
#Function that loads the key from the directory "key.key"
def loading_key():   
        return open("key.key", "r+b").read()

#Encrypting the message into bytes
key_writing()
k = loading_key()
encrypted_message = message.encode()
f = Fernet(k)
encrypted = f.encrypt(encrypted_message)
   
#ask the user for the image that is used to hide the message
image = input("Write the name of the image that is being used: ")

#creating the secret image
secret_image = lsb.hide (path, encrypted)
#saving the image
secret_image.save(message)

#reveal the message
print(lsb.reveal(path))

#decrypt the AES message
decrypted = f.decrypt(encrypted)
#convert back to string
original_message = decrypted.decode()
print("Your original message is: " + original_message)


