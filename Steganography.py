from stegano import lsb, lsbset
from stegano.lsbset import generators
from pathlib import Path
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
   
#ask the user for the image and its path that is used to hide the message
image = input("Write the name and type of the image that is being used: ")
search_path = input("Which drive is the file located in?: ")

#Finding the image
def file_search(image, search_path):
 data_folder = Path(search_path)
 file_open = data_folder / image
 f = open(file_open)
return file_open
#Calling the function
file_search(image, search_path)

#creating the secret image
secret_image = lsb.hide (file_open, encrypted)
#saving the image
secret_image.save("secret.png")

#reveal the message
lsb.reveal("secret.png")

#decrypt the AES message
decrypted = f.decrypt(encrypted)
#convert back to string
original_message = decrypted.decode()
print("Your original message is: " + original_message)


