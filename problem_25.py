# -*- coding: utf-8 -*-
def  fibonacci(n):
    fn1 = 1
    fn2 = 1
    if n<2:
        return fn1
    for i in xrange(2,n):
        fn = fn1 + fn2
        fn2 = fn1 
        fn1 = fn
    return fn1
    

print fibonacci(12)
i = 12
f = 0
while True:
    f = fibonacci(i)
    if len(str(f))==1000:
        break
    i +=1

print "%s-th fib number has 1000 digits" % i