# -*- coding: utf-8 -*-
"""
Large sum
Problem 13
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

....
"""
def main():
    f = open('problem_13.txt')
    s= 0
    for line in f.readlines():
        s  += int(line[:12])
    print "".join(list(str(s))[:10])
    f.close()


if __name__ == '__main__':main()