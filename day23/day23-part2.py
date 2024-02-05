from collections import defaultdict
dir=[(-1,0),(1,0),(0,-1),(0,1)]
def create_graph(array,rows,cols):
    d=defaultdict(list)
    d_repr={}
    for x in range(rows):
        for y in range(cols):
            if array[x][y]!='#':
                for dx,dy in dir:
                    if 0<=dx+x<rows and 0<=dy+y<cols and array[dx+x][dy+y]!='#':
                        d[(x,y)].append(tuple([dx+x,dy+y]))
                        d_repr[(x,y)]=(x,y)
    return d,d_repr

def reduce(array,rows,cols,d,d_repr):
    points=[]
    for k,v in d.items():
        if len(v)>2:
            points.append(k)
    seen2=set()
    for p in points:
        
        for i in d[p]:
            if i in seen2:
                continue
            seen={p,i}
            seen2.add(p)
            seen2.add(i)
            representation=i
            d_repr[i] = representation
            while i not in points:
                neighbours=d[i]
                i=neighbours[0] if neighbours[0] not in seen else neighbours[1] if len(neighbours)>=2 else p
                d_repr[i] = representation
                seen.add(i)
                seen2.add(i)
    new_d=defaultdict(list)
    for p in points:
        for i in d[p]:
            new_d[d_repr[i]].append(p)
            new_d[p].append(d_repr[i])
        d_repr[p]=p
    return new_d,d_repr

def func(x, y, dest_x, dest_y, d,d_repr):
    stack = [(d_repr[(x,y)][0],d_repr[(x,y)][1], [])]
    paths = []

    while stack:
        x, y, path = stack.pop()
        if (x, y) in path:
            continue
        path.append((x, y))
        if (x,y)==d_repr[(dest_x,dest_y)]:
            paths.append(path.copy())
        else:
            for neighbours in d[(x,y)]:
                stack.append((neighbours[0],neighbours[1], path.copy()))  # Down
    return paths


if __name__ == '__main__':
    with open(file='input.txt') as f:
        lines = f.readlines()
    array = [list(i[:-1]) for i in lines]
    rows = len(array)
    cols = len(array[0])
    vert,d2=create_graph(array,rows,cols)
    d,d2=reduce(array,rows,cols,vert,d2)
    values = {i:len([j for j in d2.values() if j==i]) for i in (set(d2.values()))}
    vals=func(0, 1, rows-1, cols-2, d,d2)
    maxi=-1
    for i in vals:
        maxi=max(maxi,(sum(map(lambda x:values[x],i))))
    print(maxi-1)