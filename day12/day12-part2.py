import re
from functools import cache

@cache
def fun(code,group):    
    #BASE
    if (len(group)==0):
        if '#' not in code:
            return 1
        else:
            return 0
    if len(code)==0:
        return 0

    def first_character_hashtag():   
        if '.' in set(code[:group[0]]) or len(code[:group[0]])!=group[0]: 
            return 0

        if len(code)==group[0]:
            if len(group)==1:
                return 1
            else:
                return 0
        if code[next_group] in "?.":
            return fun(code[next_group+1:], group[1:])

        return 0
    def first_character_dot():
        return fun(code[1:],group)
    
    
    next_group=group[0]

    if code[0]=='#':
        res=first_character_hashtag()
    elif code[0]=='.':
        res=first_character_dot()
    else:
        res=first_character_dot()+first_character_hashtag()
    
    print(code, group, "->", res)
    return res

if __name__=='__main__':
    with open(file='sample_input.txt') as f:
        lines=f.readlines()
    m=0
    for i in lines:
        x=i.strip().split(' ')
        code=(5*(x[0]+'?'))[:-1]
        occurences=list(map(int,x[1].split(',')))*5
        m+=(fun(code,tuple(occurences)))
    print(m)