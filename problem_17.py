# -*- coding: utf-8 -*-
"""
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def main():
    words = [len('zero'),len('one'),len('two'),len('three'),len('four'),len('five'),len('six'),len('seven'),len('eight'),len('nine')]
    #letters = map(hash,range(1,1001))
    number = "".join(map(str,range(1,6)))
    print number
    print hash(number,words)
        
def hash(n,words):
    l = map(int,list(str(n)))
    return sum(map(lambda x: words[x] ,l))
    
    
if __name__ == '__main__':main()