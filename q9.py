'''
Created on May 13, 2013

@author: Ferhawn
'''
from math import *

def nextSquare(n):
    return (sqrt(n)+1)**2


def main():
    '''
    c=5
    b=4
    a=3
    '''
    for a in range(0,1000):
        for b in range(a+1,1000):
            for c in range(b+1,1000):
                if( (a*a)+(b*b)==(c*c) and a+b+c==1000):
                    print 'done'
                    print 'a: ' + str(a)
                    print 'b: ' + str(b)
                    print 'c: ' + str(c)
                    print 'abc: ' + str(a*b*c)
                    break
        

if __name__ == "__main__":
    main()   
