#Ask user for a message
message = input("Enter a message: ")

#Cipher text variable
encoded = ''

#For loop that reverses the message
for i in range(len(message) - 1 ,-1, -1):
    encoded += message[i]

#Print encrypted text
print(encoded)
