import re
from itertools import combinations
import math

def check_len_groups(a):
    a=("".join(a)).replace('?','.')
    a=[j for j in a.split('.') if j!='']
    return list(map(lambda d: len(d),a))

def check_valid(a,b):
    for i,j in zip(a,b):
        if i!='?' and i!=j:
            return False
    return True

if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    m=0

    for id,i in enumerate(lines):
        x=i.split(' ')
        code=x[0]
        s=0
        occurences=list(map(int,x[1].split(',')))
        a=[i for i in code]
        indexes=[j for j in range(len(a)) if a[j]=='?']
        number_of_sharp=sum(occurences)
        number_of_sharp_in_code=a.count('#')
        nr_groups=len(occurences)
        for j in combinations(indexes,number_of_sharp-number_of_sharp_in_code):
            s=a.copy()
            for k in j:
                s[k]='#'
            if check_valid(a,s) and occurences==check_len_groups(s):
                m+=1
        print(m)
            

    print(m)        
        
