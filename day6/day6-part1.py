from functools import reduce
def number_of_ways(time,distance):
    r=0
    for i in range(1,time):
        if (time-i)*i>distance:
            r+=1
    return r
        

if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    times=[]
    distances=[]
    times=lines[0][lines[0].index(':')+1:].split()
    distances=lines[1][lines[1].index(':')+1:].split()
    print(reduce(lambda a,b:a*b,map(lambda a,b:number_of_ways(a,b),map(int,times),map(int,distances))))