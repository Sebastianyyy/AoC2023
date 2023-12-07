from functools import total_ordering
from collections import Counter
d={
    'A':13,
    'K':12,
    'Q':11,
    'J':10,
    'T':9,
    '9':8,
    '8':7,
    '7':6,
    '6':5,
    '5':4,
    '4':3,
    '3':2,    
    '2':1
}
@total_ordering
class Cart:
    def __init__(self,strength,bid):
        self.strength=strength
        self.bid=bid
    def __eq__(self, other):
        return self.strength==self.other
    def __lt__(self, other):
        a=Counter(self.strength).values()
        b=Counter(other.strength).values()
        if len(a)==len(b):
            
            if len(a)==2:
                if (max(a)==4 and max(b)==4) or (max(a)==3 and max(b)==3):
                    for i,j in zip(self.strength,other.strength):
                        if d[i]>d[j]:
                            return False
                        elif d[i]<d[j]:
                            return True
                else:
                    return False if max(b)==3 else True
                    
            #4,1
            #3,2
            elif len(a)==3:
                if (max(a)==3 and max(b)==3) or (max(a)==2 and max(b)==2):
                    for i,j in zip(self.strength,other.strength):
                        if d[i]>d[j]:
                            return False
                        elif d[i]<d[j]:
                            return True
                else:
                    return False if max(b)==2 else True
            #3,1,1
            #2,2,1
            else:
                for i,j in zip(self.strength,other.strength):
                    if d[i]>d[j]:
                        return False
                    elif d[i]<d[j]:
                        return True
                
        return len(a)>len(b)
if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    hands=[Cart(*i.split()) for i in lines]
    hands.sort()
    l=len(hands)
    s=0
    for i in range(l):
        s+=int(hands[i].bid)*(i+1)
    print(s)
    for i in hands:
        print(i.strength)