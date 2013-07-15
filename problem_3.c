#include<stdio.h>
#include <math.h> 

long max_prime_factor(long n){
	long z = n;
	long max_value = 0;
	long d = 2;
	n = (int) sqrt(n)+1;
	while(d < n){
		if(z%d==0){
			z /= d;
			if(d >0){
				max_value = d;
			}
		} else {
			d++;
		}
	}
	return max_value;
}

int main(void){
	long max_factor = max_prime_factor(600851475143);
	printf("max prime factor: %lu\n",max_factor);
	return 0;
}
