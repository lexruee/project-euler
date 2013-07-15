# -*- coding: utf-8 -*-
"""
Largest product in a series
Problem 8
Find the greatest product of five consecutive digits in the 1000-digit number.

...
"""
from operator import mul

def main():
    f = open('problem_8.txt')
    
    numbers = list()
    for line in f.readlines():
        for number in map(int,list(line.strip())):
            numbers.append(number)
    f.close()
    maxValue = 0
    for s in range(0,len(numbers)-5):
        v = reduce(mul,numbers[s:s+5])
        maxValue = v if maxValue < v else maxValue
    
    print maxValue

if __name__ == '__main__':main()