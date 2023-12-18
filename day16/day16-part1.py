directions={}
import time
if '__main__'==__name__:
    with open(file='input.txt') as f:
        lines=f.readlines()
    array=[list(i[:-1]) for i in lines]
    array_energized=[list(len(i[:-1])*".") for i in lines]
    array_2=[list(len(i[:-1])*".") for i in lines]
    print
    beams=[((0,0),"R")]
    while True:
        beams=[i for i in beams if i[0][0]>=0 and i[0][0]< len(array[0]) and i[0][1]>=0 and i[0][1]<len(array) and not i[1] in array_2[i[0][0]][i[0][1]]]
        if not beams:
            break
        for ((x,y),dir) in beams:
            array_energized[x][y]="#"
        for (id,((x,y),dir)) in enumerate(beams):
            array_2[x][y]=array_2[x][y]+dir
            if dir=='R':
                if array[x][y]=='.':
                    beams[id]=((x,y+1),"R")
                elif array[x][y]=='/':
                    beams[id]=((x-1,y),"U")
                elif array[x][y]=='\\':
                    beams[id]=((x+1,y),"D")
                elif array[x][y]=='|':
                    beams[id]=((x+1,y),"D")
                    beams.append(((x,y),"U"))
                else:
                    beams[id]=((x,y+1),"R")
                
            elif dir=='L':
                if array[x][y]=='.':
                    beams[id]=((x,y-1),"L")
                elif array[x][y]=='/':
                    beams[id]=((x+1,y),"D")
                elif array[x][y]=='\\':
                    beams[id]=((x-1,y),"U")
                elif array[x][y]=='|':
                    beams[id]=((x+1,y),"D")
                    beams.append(((x,y),"U"))
                else:
                    beams[id]=((x,y-1),"L")
                    
            elif dir=='U':
                if array[x][y]=='.':
                    beams[id]=((x-1,y),"U")
                elif array[x][y]=='/':
                    beams[id]=((x,y+1),"R")
                elif array[x][y]=='\\':
                    beams[id]=((x,y-1),"L")
                elif array[x][y]=='|':
                    beams[id]=((x-1,y),"U")
                else:
                    beams[id]=((x,y-1),"L")
                    beams.append(((x,y),"R"))
            else:
                if array[x][y]=='.':
                    beams[id]=((x+1,y),"D")
                elif array[x][y]=='/':
                    beams[id]=((x,y-1),"L")
                elif array[x][y]=='\\':
                    beams[id]=((x,y+1),"R")
                elif array[x][y]=='|':
                    beams[id]=((x+1,y),"D")
                else:
                    beams[id]=((x,y-1),"L")
                    beams.append(((x,y),"R"))
        #print(beams)
        #time.sleep(1)
    s=0
    for i in array_energized:
        t=("".join(i))
        s+=t.count('#')
    print(s)
