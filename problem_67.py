import problem_18
import time
f = open('problem_67_triangle.txt')

def main():
    grid = list()
    for line in f.readlines():
        grid.append(map(int,list(line.strip().split())))
    
    f.close()   
    
    start = time.time()
    print problem_18.solve(grid)
    end = time.time()
    print "time: %s" % (end-start)
    
if __name__== "__main__":main()