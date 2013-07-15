"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math
import time

def max_prime_factor(n):
    z = n
    max_value = 0
    d=2
    n = math.sqrt(n)+1
    while d < n:
        if z%d==0:
            z /= d
            if d > 0:
                max_value = d
        else:
            d +=1
    return max_value
start = time.time()
print max_prime_factor(600851475143)
end = time.time()

print "time: %s " % (end-start)