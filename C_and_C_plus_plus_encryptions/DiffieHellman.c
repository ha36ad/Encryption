#include <stdio.h>
// Function to compute Key Formulas
int key_compute(int x, int y, int p)
{
	int m;
	int n = 1;

	while (y > 0)
	{
		m = y % 2;

		if (m == 1)
		  n = (n*x) % p;
		  x = x*x % p;

		y = y / 2;
	}

	return n;
} 
//Main function
int main()
{
  //Modulus
  int p = 941;  
  //Base
  int g = 527;
  
  // a = Alice's secret key, b = Bob's secret key, A = Alice's Public Key, B = Bob's Public Key
  int a, A, b, B;
  a = 347;
  b = 781;
  
  // Calculate Bob's public key
 B = key_compute(g, b, p);
  //Calculate Alice's public key
 A = key_compute(g, a, p);
    
  //Calcuate Bob's secret key
  int KeyB = key_compute (A, b, p);
  //Calculate Alice's secret key
  int KeyA = key_compute (B, a, p);
  
  //Printing the keys
  printf("Bob's Secret Key is %d\n Alice's Secret Key is %d", KeyB, KeyA);
  return 0;
 
}
