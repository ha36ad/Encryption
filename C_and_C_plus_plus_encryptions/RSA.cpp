#include <iostream>
#include <math.h>
using namespace std;

//Finding the GCD
int gcd(int a, int b) 
{
    int t;
    while(1){
      t = a%b;
      if (t==0)
        return b;
      a = b;
      b = t;
    }
}

int main()
{
    //Prime numbers
   double p = 13;
   double q = 11;
   double n = p*q;
  //Message length
  double message = 9;
  //Totient function
   double phi = (p-1)*(q-1);
   
   //Public Key
  double encrypt = 7;

  //Check if public key is co-prime to phi
  while (encrypt<phi)
  {
      if (gcd(encrypt,phi)== 1)
        break;
      else
        encrypt++;
  }

  //Private Key
   //Ensure that d*e = 1 mod phi
  double d = 1/encrypt;
  double decrypt = fmod(d,phi);

  //Encrypting message
  double c = pow(message,encrypt);
  //Decrypting message
  double m = pow(c,decrypt);
  m = fmod(m,n);
  c = fmod(c,n);
  //Printing the original, encrypted, and decrypted message
  cout<<"Original Message: "<<message;
  cout<<"\n"<<"Encrypted Message: "<<c;
  cout<<"\n"<<"Decrypted message: "<<m;
  return 0;
}
