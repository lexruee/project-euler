# -*- coding: utf-8 -*-
import math
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
def lcm(a,b):
    return math.fabs((a*b)/gcd(a,b))

def lcm_loop(t,i):
    return lcm_loop(t[i:])
    
print gcd(18,12)
print lcm(12,18)
t = range(1,11)
print lcm_loop(lcm(t[0],t[1]),t,0)