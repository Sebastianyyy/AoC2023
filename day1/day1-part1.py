import re

score=0
if __name__=='__main__':
    with open(file='day1input.txt') as f:
        lines=f.readlines()
    
    for line in lines:
        pattern_first=r'^[a-zA-Z]*([0-9]).*$'
        pattern_second=r'^.*([0-9])[a-zA-Z]*$'
        x=re.search(pattern=pattern_first,string=line)
        y=re.search(pattern=pattern_second,string=line)
        score+=int(x.group(1)+y.group(1))
    print(score)