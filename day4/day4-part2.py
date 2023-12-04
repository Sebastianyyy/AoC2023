if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    s=0
    d={}
    for id,i in enumerate(lines,start=1):
        d[id]=d.get(id,0)+1
        e=i.split('|')
        winning_numbers=e[0][e[0].find(':')+1:].split()
        having_numbers=e[1].split()
        l=len(set(having_numbers)&set(winning_numbers))
        for i in range(l):
            d[id+i+1]=d.get(id+i+1,0)+1*d[id]
    print(sum(d.values()))
