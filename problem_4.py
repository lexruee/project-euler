# -*- coding: utf-8 -*-
"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import math
import time
def is_palindrome(p):
    s = str(p)
    o = 1 if len(s) % 2!=0 else 0
    part = s[:int(math.floor(len(s)/2))]
    reverse_part = s[int(math.ceil(len(s)/2))+o:]
    return part == reverse_part[::-1]
        

def main():
    start = time.time()
    m = 0
    n1 = 999
    while n1 > 900:
        n2 = 999
        while n2>900:  
            p = n1 * n2
            if is_palindrome(p) and p > m:
                m = p
            
            n2 -=1
        n1 -=1
    end = time.time()
    print m
    print "time: %s" % (end-start)
    
if __name__=="__main__": main()