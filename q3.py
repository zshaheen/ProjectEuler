'''
Created on May 7, 2013

@author: New Desktop
'''

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
    if( ((2**n)%n) == 2): 
        return True
    else:
        return False

'''600851475143'''
def main():

    x=600851475143
    a=2
    largestPrime=0
    
    while (x!=1):
        if(x%a==0):
            largestPrime=a
            x=x/a
            a=1
        a=nextPrime(a)
    print 'largestPrime: '
    print largestPrime


if __name__ == "__main__":
    main()    
    