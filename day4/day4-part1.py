if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    s=0
    for i in lines:
        e=i.split('|')
        winning_numbers=e[0][e[0].find(':')+1:].split()
        having_numbers=e[1].split()
        l=len(set(having_numbers)&set(winning_numbers))-1
        res=2**l if l>=0 else 0
        s+=res
    print(s)
