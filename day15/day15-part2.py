from collections import defaultdict
def get_hash_sum(s):
    curr=0
    for i in s:
        curr=((curr+ord(i))*17)%256
    return curr
if __name__=='__main__':
    d=defaultdict(list)
    s=0
    with open(file='input.txt') as f:
        lines=f.readlines()
    for i in lines[0].split(','):
        if '-' in i:
            h=get_hash_sum(i[0:-1])
            temp=[j for j in d[h] if j[0:-2]!=i[0:-1]]
            d[h]=temp
        else:
            h=get_hash_sum(i[0:-2])
            if any(j[0:-2]==i[0:-2] for j in d[h]):
                temp=[j if j[0:-2]!=i[0:-2] else i for j in d[h]]
                d[h]=temp
            else:
                d[h].append(i)
    for k,v in d.items():
        for i,value in enumerate(v,1):
            s+=(k+1)*(i)*(int(value[-1]))
    print(s)