from typing import Any
import re

class Condition:
    def __init__(self,element:str,cond:str,number:str,accept:str):
        self.element=element
        self.cond=cond
        self.number=number
        self.accept=accept
    def __str__(self):
        return f"{self.element},{self.cond},{self.number},{self.accept}"

    def check(self,elements):
        for element,number in elements:
            if element==self.element and eval(number+self.cond+self.number):
                return True,self.accept
        return False,-1
class Workflow:
    def __init__(self,name:str,conditions:str):
        self.name=name
        c,self.else_=self.split_to_conditionals(conditions)
        self.conditionals=self.make_conditions(c)
    def split_to_conditionals(self,s:str):
        s=s[1:-1]
        l=s.split(',')
        return l[:-1],l[-1]
        
    def make_conditions(self,li):
        arr=[]
        pattern=r'(\w+)([><])(\d+):(\w+)'
        for i in li:
            x=re.search(pattern=pattern,string=i)
            arr.append(Condition(x.group(1),x.group(2),x.group(3),x.group(4)))
        
        return arr

    def __call__(self,elements):
        for i in self.conditionals:
            x=i.check(elements)
            if x[0]:
                return x[1]
        return self.else_
            

if __name__=='__main__':
    s=0
    d=dict()
    with open(file='input.txt') as f:
        lines=f.readlines()
    i=0
    while lines[i]!='\n':
        k=lines[i].index('{')
        x=Workflow(lines[i][:k],lines[i][k:-1])
        d[lines[i][:k]]=x
        i+=1
    i+=1
    s=0
    while lines[i]!='\n':
        arr=[(j[0],j[2:]) for j in lines[i][1:-2].split(',')]
        curr_state='in'
        while curr_state not in {"R","A"}:
            #print(curr_state)
            curr_state=d[curr_state](arr)
        if curr_state=='A':
            s+=sum([int(i[1]) for i in arr])
        i+=1
    print(s)