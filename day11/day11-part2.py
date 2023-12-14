import numpy as np
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    @staticmethod
    def distance(a,b,rows,cols):
        r=[i for i in rows if (a.x>i>b.x or b.x>i>a.x)]
        c=[i for i in cols if (a.y>i>b.y or b.y>i>a.y)]

        return abs(a.x-b.x)+abs(a.y-b.y)+len(r)*(1000000-1)+len(c)*(1000000-1)
    
if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    big_universes_row=[]
    big_universes_col=[]
    array=(np.vstack([list(i[:-1]) for i in lines]))
    points=[]
    size=array.shape
    for i in range(size[0]):
        for j in range(size[1]):
            if array[i,j]=='#':
                points.append(Point(i,j))
        if set(array[i,:])=={'.'}:
            big_universes_row.append(i)
    for i in range(size[1]):
        if set(array[:,i])=={'.'}:
            big_universes_col.append(i)
    s=0
    for i in range(len(points)):
        for j in range(i,len(points)):
            s+=Point.distance(points[i],points[j],big_universes_row,big_universes_col)
    print(s)