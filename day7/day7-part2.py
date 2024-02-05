from functools import total_ordering
from collections import Counter
d={'A':13,'K':12,'Q':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2,'J':1}
@total_ordering
class Cart:
    def __init__(self,strength,bid,old_strength):
        self.strength=strength
        self.bid=bid
        self.old_strength=old_strength
    def __eq__(self, other):
        return self.strength==self.other
    def __lt__(self, other):
        a=Counter(self.strength).values()
        b=Counter(other.strength).values()
        if len(a)==len(b):
            if len(a)==2:
                if (max(a)==4 and max(b)==4) or (max(a)==3 and max(b)==3):
                    for i,j in zip(self.old_strength,other.old_strength):
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
                    for i,j in zip(self.old_strength,other.old_strength):
                        if d[i]>d[j]:
                            return False
                        elif d[i]<d[j]:
                            return True
                else:
                    return False if max(b)==2 else True
            #3,1,1
            #2,2,1
            else:
                for i,j in zip(self.old_strength,other.old_strength):
                    if d[i]>d[j]:
                        return False
                    elif d[i]<d[j]:
                        return True
                
        return len(a)>len(b)
    def __str__(self) -> str:
        return f'{self.strength}, {self.bid}, {self.old_strength}'
if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    hands=[]
    for i in lines:
        x=i.split()
        if 'J' in x[0]:
            if len(set(x[0])-set("J"))==0:
                a="AAAAA"
            else:
                a=x[0].replace('J',max(set(x[0])-set("J"), key = x[0].count))
            hands.append(Cart(a,x[1],x[0]))
        else:
            hands.append(Cart(x[0],x[1],x[0]))

    s=0    
    hands.sort()
    for id,i in enumerate(hands,start=1):
        s+=id*int(i.bid)
        print(i)
    print(s)