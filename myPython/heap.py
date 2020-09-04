import heapq

l =[1,3,4, 5,0,9]
heap = heapq.heapify(l)
print(heapq.nlargest(3, l))
