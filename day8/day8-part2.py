from itertools import cycle
import math

if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    d={}
    instructions=lines[0].strip()
    
    for i in lines[2:]:
        key=i[0:3]
        value=tuple([i[7:10],i[12:15]])
        d[key]=value
    s=0
    keys=[i for i in d.keys() if i[-1]=='A']
    l=[]
    for k in keys:
        s=0
        for i in cycle(instructions):
            s+=1
            k= d[k][0] if i=='L' else d[k][1]
            if k[-1]=="Z":
                break
        l.append(s)
    print(math.lcm(*l))
