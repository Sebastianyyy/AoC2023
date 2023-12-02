import re

if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    
    d={}
    sum=0
    for id,line in enumerate(lines,start=1):
        flag=True
        for i in line.split(';'):
            if x:=re.search(pattern=r'(\d+) blue',string=i):
                if int(x.group(1))>14:
                    flag=False
            if x:=re.search(pattern=r'(\d+) red',string=i):

                if int(x.group(1))>12:
                    flag=False
            if x:=re.search(pattern=r'(\d+) green',string=i):

                if int(x.group(1))>13:
                    flag=False
        if flag:
            sum+=id
    print(sum)