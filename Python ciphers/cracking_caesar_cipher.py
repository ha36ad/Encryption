import string

upper_case = list(string.ascii_uppercase)
lower_case = list(string.ascii_lowercase)

#Ask user for a message
message = input("Enter the encrypted message: ")


#Breaking cipher:
for j in range(26):
    decrypted_text = ""
    for i in message:
        if  i in upper_case:
            decrypted_text += (upper_case[(upper_case.index(i) + j  - 26)])
     
        elif i in lower_case:
                decrypted_text += (lower_case[(lower_case.index(i) + j - 26)])
    print(j, ":" ,decrypted_text)
