import re

score=0
if __name__=='__main__':
    with open(file='day1input.txt') as f:
        lines=f.readlines()
    
    d={
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }
    pattern_first='^.*?('+"|".join(d.keys())+'|[0-9]).*$'
    pattern_second='^.*('+"|".join(d.keys())+'|[0-9]).*$'

    for line in lines:
        x=re.search(pattern=pattern_first,string=line)
        y=re.search(pattern=pattern_second,string=line)
        score+=int(d.get(x.group(1),x.group(1))+d.get(y.group(1),y.group(1)))
        print(d.get(x.group(1),x.group(1))+d.get(y.group(1),y.group(1)))
    print(score)