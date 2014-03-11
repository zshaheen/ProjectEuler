'''
Created on May 12, 2013

@author: Zeshawn
'''
import random 
import math

def nextPrime(n):
    '''n=n+1'''
    if(n<=1):
        return 2
    n=n+1
    while isPrime(n)==False:
        n=n+1
    return n

def isPrime(n):
    '''2<=2<=n-1'''
    ''' we have multiple rand nums to test to eliminate change of psuedoprimes '''
    '''
    random.seed()
    rnd = random.randint(2,n-1)
    rnd2 = random.randint(rnd,n-1)
    rnd3 = random.randint(rnd,n-1)
    if( ((rnd**n)%n) == rnd and ((rnd2**n)%n == rnd2) and ((rnd3**n)%n == rnd3)): 
        return True
    else:
        return False
    '''
    
    ''' if n is even, then it is not prime'''
    if (n%2==0):
        return False
    n_orig = n
    n=n-1
    while (n%2==0):
        n=n/2
    '''now n is d such that n-1 = (2^s)*d'''
    a = random.randint(2,n_orig-1)
    if (a**n)%n_orig == 1 or (a**n)%n_orig == -1:
        return True
    else:
        s=math.log((n_orig-1)/n,2)
        print 's: '
        print s
        exponent=0
        while exponent<=(2**(s-1)):
            exponent=
            
            
            
            exponent=exponent+2


def main():
    
    
    prime = 1
    x=0
    while x<22:
        prime = nextPrime(prime)
        x=x+1
    print prime
    '''
    print isPrime(341)
    print nextPrime(338)
    '''
if __name__ == "__main__":
    main()   
