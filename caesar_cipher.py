import string

upper_case = list(string.ascii_uppercase)
lower_case = list(string.ascii_lowercase)

#Ask user for a message
message = input("Enter a message: ")

#Ask user for shift value
key = int(input("Enter the shift value (negative for left, postive for right): "))

#Encrypted message:
encrypted_text = ""
for i in message:
    if  i in upper_case:
     encrypted_text += (upper_case[(upper_case.index(i) +  10 - 26)])
     
    elif i in lower_case:
        encrypted_text += (lower_case[(lower_case.index(i) + key - 26)])

print(encrypted_text)
