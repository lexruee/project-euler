# -*- coding: utf-8 -*-
"""
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import problem_7
import time


def main():
    start = time.time()
    
    primes = list()
    p = 2
    limit = 2*10**6
    while p <=limit:
        if problem_7.is_prime(p):
            primes.append(p)
            
        p +=1
        
    print sum(primes)
    end = time.time()
    print "time: %s" % (end-start)


if __name__ == '__main__':main()