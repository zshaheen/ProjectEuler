'''
Created on May 7, 2013

@author: New Desktop
'''
sum=0
for x in range(1,1000):
    if (x%3==0 or x%5==0):
        sum = sum + x
print sum