# -*- coding: utf-8 -*-
import time

def solve(grid):
    table = grid[:]
    table.reverse()
    for k in range(0, len(table) - 1):
        for i in range(0, len(table[k]) - 1): 
            table[k + 1][i] = table[k + 1][i] + max(table[k][i], table[k][i + 1]) 
    return table[len(table) - 1][0] 
    
def  main():
    f = open('problem_18.txt')
    
    grid = list()
    for line in f.readlines():
        grid.append(map(int,list(line.strip().split())))
    f.close()   
    
  
        
    start = time.time()
    print solve(grid)
    end = time.time()
    print "time: %s" % (end-start)

if __name__== "__main__":main()
