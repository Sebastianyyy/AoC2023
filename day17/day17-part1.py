import time
import sys
import heapq
directions={"L":["L","U","D"],
            "R":["R","U","D"],
            "U":["R","L","U"],
            "D":["R","D","L"],
            "-1":["R","D"]}

def func(x_end,y_end,array,rows,cols):
    memo=set()
    heap=[(0,0,0,"-1",-1)]#dist,x,y,dir,range
    while heap:
        dist,x,y,direction,range=heapq.heappop(heap)
        if x==x_end and y==y_end:
            return dist
        if (x,y,direction,range) in memo:
            continue
        memo.add((x,y,direction,range))
        for i in directions[direction]:
            if i=='L':
                x_new,y_new=x,y-1
            elif i=='R':
                x_new,y_new=x,y+1
            elif i=='U':
                x_new,y_new=x-1,y
            else :#D
                x_new,y_new=x+1,y            
            r_new=(1 if i!=direction else range+1)
            if rows<=x_new or x_new<0 or 0>y_new or y_new>=cols or (x_new,y_new,i,r_new) in memo or r_new>3:
                continue
            cost=int(array[x_new][y_new])
            heapq.heappush(heap,(dist+cost,x_new,y_new,i,r_new))

if __name__=='__main__':
    s=0
    with open(file='input.txt') as f:
        lines=f.readlines()
    array=[list(i[:-1]) for i in lines]
    rows=len(array)
    cols=len(array[0])
    print(func(rows-1,cols-1,array,rows,cols))

