# -*- coding: utf-8 -*-
"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from math import sqrt
import time


def is_prime(n):
    if n==1:
        return False
    if n==2:
        return True
    if n == 3:
        return True
    if n%2==0:
        return False
    if n%3==0:
        return False
    r = int(sqrt(n)+1)
    f = 5
    while f<=r:
        if n % f==0:
            return False
        if n % (f+2)==0:
            return False
        f +=6
    return True

def main(): 
    start = time.time()
    limit = 10001
    counter = 0
    number = 2
    while True:
        if is_prime(number):
            counter +=1
         
        if counter==limit:
            break
        
        number += 1
    
    print number
    
    end = time.time()
    print "time: %s" % (end-start)
    
if __name__ == '__main__':main()

