'''
Created on May 12, 2013

@author: Zeshawn
'''
    
    
def isPalindrome(n):
    string = str(n)
    length = len(string)
    i=0
    while i<length//2:
        if string[i]!= string[length-i-1]:
            return False
        i=i+1
    return True
        
def main():
    x=100
    y=100
    largestPalindrome=0
    while (y!=1000):
        while x<1000:
            if (isPalindrome(x*y)==True and largestPalindrome<(x*y)):
                largestPalindrome = x*y
            x=x+1
        y=y+1
        x=100
        
    print largestPalindrome
    

if __name__ == "__main__":
    main()    
    


