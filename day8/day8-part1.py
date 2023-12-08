from itertools import cycle


if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    d={}
    instructions=lines[0].strip()
    
    for i in lines[2:]:
        key=i[0:3]
        value=tuple([i[7:10],i[12:15]])
        d[key]=value
    k="AAA"
    s=0
    print(list(instructions))
    for i in cycle(instructions):
        s+=1
        k= d[k][0] if i=='L' else d[k][1]
        print(k)
        if k=="ZZZ":
            break
    print(s)
