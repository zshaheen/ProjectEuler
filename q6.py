'''
Created on May 12, 2013

@author: Zeshawn
'''

x=1
y=1
''' 1^2 + 2^2 + ... +10^2_'''
sumOfSquare=0
''' (1+2+...+10)^2 '''
squareOfSum=0

'''Sum of squares'''
while x<=100:
   sumOfSquare = sumOfSquare + (x*x)
   x=x+1

'''Square of sum'''
while y<=100:
   squareOfSum = squareOfSum + y
   y=y+1
   
squareOfSum = squareOfSum **2

print squareOfSum - sumOfSquare



   




