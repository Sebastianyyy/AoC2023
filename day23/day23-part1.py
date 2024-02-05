from functools import cache
from copy import deepcopy

opportunities={""}

def func(array, x, y, dest_x, dest_y, rows, cols, mat_copy, curr=0, ans=-1):
    visited=[[False for j in range(cols)] for i in range(rows)]
    stack = [(x, y, [])]
    paths = []

    while stack:
        x, y, path = stack.pop()

        if x < 0 or x >= rows or y < 0 or y >= cols or array[x][y] == '#' or (x, y) in path:
            continue

        path.append((x, y))

        if x == dest_x and y == dest_y:
            paths.append(path.copy())
        else:
            if array[x][y]=='>':
                stack.append((x, y + 1, path.copy())) 

            elif array[x][y]=='<':
                stack.append((x, y - 1, path.copy()))  
               
            elif array[x][y]=='^':
                stack.append((x - 1, y, path.copy()))  
 
            elif array[x][y]=='v':
                stack.append((x + 1, y, path.copy()))  

            else:
                stack.append((x + 1, y, path.copy()))  
                stack.append((x - 1, y, path.copy()))  
                stack.append((x, y + 1, path.copy()))  
                stack.append((x, y - 1, path.copy()))  

    longest_path = max(paths, key=len) if paths else []
    return len(longest_path)-1

    
if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    array=[list(i[:-1]) for i in lines]
    rows=len(array)
    cols=len(array[0])
    visited = [[False for i in range(cols)]for j in range(rows)]
    print(func(array,0,1,rows-1,cols-2,rows,cols,deepcopy(array)))
