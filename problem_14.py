# -*- coding: utf-8 -*-
"""
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import time
 
def length(n):
    counter = 1
    while True:
        if n%2==0:
            n = n/2
        else:
            n = 3*n+1
        counter +=1
        if n==1:
            return counter

def main():
    start = time.time()
    t = (0,1)
    for i in range(1,10**6):
        l = length(i)
        m = (l,i)
        if m[0] > t[0]:
            t = m
        
    print "len: %s, start number: %s" % t
    end = time.time()
    print "time: %s " % (end-start)
    
    
if __name__ == '__main__':main()
    