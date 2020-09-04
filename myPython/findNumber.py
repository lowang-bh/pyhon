#!/usr/bin/env python

def find(lsData, num):
    lenth = len(lsData)
    i, j = 0, lenth - 1
    while i < j:
        if lsData[i] + lsData[j] == num:
            return True
        elif lsData[i] + lsData[j] < num:
            i+=1
        else:
            j-=1
    
    return False

if __name__=="__main__":
    l=[1,2,3,4,5,6,7,8,9,10]
    print(find(l, 12))
