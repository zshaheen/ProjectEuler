'''
Created on May 14, 2013

@author: Ferhawn
'''
'''
Created on May 7, 2013

@author: New Desktop
'''
import random 

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
    random.seed()
    rnd = random.randint(2,n-1)
    if( ((2**n)%n) == 2):
        ''' if true, run another test'''
        if( ((3**n)%n) == 3):
            '''if( ((rnd**n)%n) == rnd):'''
            return True
        else:
            return False
    else:
        return False

def main():
    prime = 1
    x=0
    while x<-1:
        prime = nextPrime(prime)
        x=x+1
    print prime


if __name__ == "__main__":
    main()    
    