'''
Created on May 7, 2013

@author: New Desktop
'''
x=1
y=2
sum=0
while (y<3999999):
    temp = y
    y = y+x
    x = temp
    if (y%2==0):
        sum = sum + y
'''plus 2 includes the y=2'''
print sum+2



