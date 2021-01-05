#include <iostream>
#include <cstring>
using namespace std;

//Encryption and Decryption Function
void Encrypt_and_Decrypt(char inputString[]) 
{
    //Calculate the length of the input string
    int length = strlen(inputString);

    //Define key, any character works
    char Key ='Q';
    
    //Apply XOR operations to each character
    for (int i = 0; i < length;i++)
    {
        inputString[i] = inputString[i] ^Key;
    }   
}
//Run the program
int main()
{
    char Test_String[] ="HelloandGoodbye";

    //Encrypted string
    Encrypt_and_Decrypt(Test_String);
    //Decrypted string
    Encrypt_and_Decrypt(Test_String);
    
    return 0;
}

