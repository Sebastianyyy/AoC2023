from itertools import cycle


if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    s=0
    for i in lines:
        numbers=list(map(int,i.split()))
        l=[]    
        m=[]
        l.append(numbers)
        while not all(j==0 for j in l[-1]):
            temp=l[-1]
            x=[]
            for first,second in zip(temp[:-1],temp[1:]):
                x.append(second-first)                
            l.append(x)
        m.append(0)
        for j in range(len(l)-2,-1,-1):
            m.append(l[j][0]-m[-1])
        print(m)
        s+=m[-1]
    print(s)