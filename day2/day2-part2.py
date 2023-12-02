import re

if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    
    d={}
    sum=0
    for line in lines:
        max_red=0
        max_blue=0
        max_green=0
        for i in line.split(';'):
            if x:=re.search(pattern=r'(\d+) blue',string=i):
                max_blue=max(max_blue,int(x.group(1)))
            if x:=re.search(pattern=r'(\d+) red',string=i):
                max_red=max(max_red,int(x.group(1)))
            if x:=re.search(pattern=r'(\d+) green',string=i):
                max_green=max(max_green,int(x.group(1)))
        sum+=max_green*max_red*max_blue
    print(sum)