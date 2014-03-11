'''
Created on May 12, 2013

@author: Zeshawn
'''

'''
i|8 -> i|4 and i|2
NOT: i|2 and i|4 -> i|8

'''

i=20
while True:
    if(i%19==0) and (i%18==0) and (i%17==0) and (i%16==0) and (i%15==0) and (i%14==0) and (i%13==0) and  (i%12==0)  and (i%11==0):
        break 
    i=i+20
print i







