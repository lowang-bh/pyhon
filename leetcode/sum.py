# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
一个无序不重复的整数数组，给一个数值 K，问有多少对数之和为K？ 有多少对之差为K？
"""

def findTarget(array, target):
    sumRes = {}
    subRes = {}
    sumNum, subNum = 0, 0 
    for item in array:
        if target - item in sumRes:
            sumNum += 1
        sumRes[item] = 0
            
        
        if target + item in subRes :
            subNum += 1
        else:
            subRes.setdefault(item, subRes.get(item, 0) + 1)
            
        if item - target in subRes:
            subNum += 1
        else:
            subRes.setdefault(item, subRes.get(item, 0) + 1)
    
    
    return sumNum, subNum
            


print(findTarget([7,9, 3,1,2,4], 5))
print(findTarget([2, 7, 2, 2, -2, 16], 9)) # 2, 2

print(findTarget([1,5,3,-1], 2)) #1, 3
print(findTarget([1, 2, 3, 4, 5],1)) # 0, 4
print(findTarget([1, 3, 1, 5, 4],0)) # 0, 1

