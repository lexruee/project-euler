# -*- coding: utf-8 -*-
"""
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""
def main():
    sq = 0
    s = 0
    for x in range(1,101):
        sq+= x**2
        s += x
    s2 = s**2
    print s2-sq

if __name__ == '__main__':main()