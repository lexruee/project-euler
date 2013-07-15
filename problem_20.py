# -*- coding: utf-8 -*-
"""
Factorial digit sum
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
def factorial(n):
    def loop(acc,n):
        if n==0:
            return acc
        else:
            return loop(acc*n,n-1)
    return loop(1,n)

def main():
    print sum(map(int,list(str(factorial(100)))))
    
if __name__=="__main__":main()