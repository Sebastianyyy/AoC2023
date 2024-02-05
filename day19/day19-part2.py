from typing import Any
import re
from itertools import chain
from collections import defaultdict 

class Node:
    def __init__(self,name,range_={"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}):
        self.name=name
        self.range_=range_

if __name__=='__main__':
    s=0
    d={}
    with open(file='input.txt') as f:
        lines=f.readlines()
    i=0
    while lines[i]!='\n':
        k=lines[i].index('{')
        string=lines[i][k+1:-2].split(',')
        d[lines[i][:k]]=string
        i+=1
    suma = 0
    q=[Node("in")]
    while q:
        node=q.pop()
        for i in d[node.name]:
            if ":" in i:
                pattern=r"(\w)([<>])(\d+):(\w+)"
                x=re.search(pattern=pattern, string=i)
                element,condition,number,cond_done=x.group(1),x.group(2),x.group(3),x.group(4)
                copy_range_=node.range_.copy()
                start=node.range_[element][0]
                end=node.range_[element][1]
                if condition == '<':
                    copy_range_[element] = (start, int(number) - 1)
                    node.range_[element] = (int(number), end)
                else:
                    node.range_[element] = (start, int(number))
                    copy_range_[element] = (int(number) + 1, end)
                if cond_done=='A':
                    suma+=(copy_range_['x'][1]-copy_range_['x'][0]+1)*(copy_range_['m'][1]-copy_range_['m'][0]+1)*(copy_range_['a'][1]-copy_range_['a'][0]+1)*(copy_range_['s'][1]-copy_range_['s'][0]+1)

                elif cond_done!='R':
                    q.append(Node(cond_done,copy_range_.copy()))
            else:
                if i == 'A': 
                    suma+=(node.range_['x'][1]-node.range_['x'][0]+1)*(node.range_['m'][1]-node.range_['m'][0]+1)*(node.range_['a'][1]-node.range_['a'][0]+1)*(node.range_['s'][1]-node.range_['s'][0]+1)
                elif i!='R':
                    q.append(Node(i, node.range_.copy()))
                    
    print(suma)