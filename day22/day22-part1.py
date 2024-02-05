import numpy as np
from collections import defaultdict
from copy import deepcopy
if __name__ == '__main__':
    s = 0
    with open(file='input.txt') as f:
        lines = f.readlines()
    max_x, max_y, max_z = 0, 0, 0
    for i in lines:
        l, r = i[:-1].split('~')
        l, r = list(map(int, l.split(','))), list(map(int, r.split(',')))
        max_x, max_y, max_z = max(max_x, l[0], r[0]), max(
            max_y, l[1], r[1]), max(max_z, l[2], r[2])
    max_x, max_y, max_z = max_x+1, max_y+1, max_z+1
    array_3d = [[[0 for _ in range(max_y)]
                 for _ in range(max_x)] for _ in range(max_z)]
    positions = defaultdict(set)
    levels = defaultdict(list)
    level_of_element=defaultdict(int)
    len_of_z = dict()
    for id, i in enumerate(lines, 1):
        l, r = i[:-1].split('~')
        l, r = list(map(int, l.split(','))), list(map(int, r.split(',')))
        for z in range(l[2], r[2] + 1):
            for x in range(l[0], r[0] + 1):
                for y in range(l[1], r[1] + 1):
                    positions[id].add((x, y))
                    if id not in [i for j in levels.values() for i in j]:
                        levels[z].append(id)
                    array_3d[z][x][y] = id
            len_of_z[id] = r[2]-l[2]+1
            level_of_element[id]=l[2]

    for z in range(2, max_z):
        array = array_3d[z]
        #print(levels[z])
        levels_copy=deepcopy(levels[z])
        for i in levels[z]:
            z2 = z
            while all([array_3d[z2-1][x][y] == 0 and z2>=2 for (x, y) in positions[i]]):
                z2 =z2-1
            if z2 != z:
                len_of_depth = len_of_z[i]
                for j in range(len_of_depth):
                    for x, y in positions[i]:
                        array_3d[z+j][x][y] = 0

                for j in range(len_of_depth):
                    for x, y in positions[i]:
                        array_3d[z2+j][x][y] = i
                levels_copy.remove(i)
                levels[z2].append(i)
                level_of_element[i]=z2
        levels[z]=levels_copy
    s=set()
    for i in range(1,len(positions)+1):
        for j in range(i+1,len(positions)+1):
            if len(positions[i]&positions[j])!=0 and level_of_element[i]!=level_of_element[j]:
                first=positions[i]-positions[j]
                second=positions[j]-positions[i]
                if level_of_element[i]==level_of_element[j]+len_of_z[j]:
                    if all(array_3d[level_of_element[i]-1][x][y] == 0 for (x, y) in first) and level_of_element[i]-1>=1:
                        s.add(j)
                        
                elif level_of_element[j]==level_of_element[i]+len_of_z[i]:
                    if all(array_3d[level_of_element[j]-1][x][y] == 0 for (x, y) in second) and level_of_element[j]-1>=1:
                        s.add(i)
    print(len(positions.keys())-len(s))
