from copy import deepcopy

mapping={
    "LEFT":(['I','J','7'],{'-':'W','L':'N','F':'S'},0,-1),
    "RIGHT":(['|','L','F'],{'-':'E','7':'S','J':'N'},0,1),
    "BOT":(['-','7','F'],{'|':'S','L':'E','J':'W'},1,0),
    "TOP":(['-','L','J'],{'|':'N','7':'W','F':'E'},-1,0)
}

def check_direction(row,column,array,direction):
    if(row+mapping[direction][2]<0 or row+mapping[direction][2]>=len(array) or column+mapping[direction][3]<0 or column+mapping[direction][3]>=len(array[0])):
        return None, None,-1,-1
    for i in mapping[direction][0]:
        if array[row+mapping[direction][2]][column+mapping[direction][3]]==i:
            return None,None,-1,-1
    for k,v in mapping[direction][1].items():
        if array[row+mapping[direction][2]][column+mapping[direction][3]]==k:
            return k,v,row+mapping[direction][2],column+mapping[direction][3]
    return "S",None,-1,-1

if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    l=[]
    for i in lines:
        l.append([x for x in i][:-1])
    k=deepcopy(l)
    row=-1
    column=-1
    length=len(l)
    for i in range(length):
        for j in range(length):
            if l[i][j]=='S':
                row=i
                column=j
    curr_state='S'
    direction=''
    if check_direction(row,column,l,"TOP")[1]:
        curr_state,direction,row,column=check_direction(row,column,l,"TOP")
    elif check_direction(row,column,l,"BOT")[1]:
        curr_state,direction,row,column=check_direction(row,column,l,"BOT")
        
    elif check_direction(row,column,l,"RIGHT")[1]:
        curr_state,direction,row,column=check_direction(row,column,l,"RIGHT")
        
    elif check_direction(row,column,l,"LEFT")[1]:
        curr_state,direction,row,column=check_direction(row,column,l,"LEFT")
    s=0
    print(curr_state,direction)
    while True:
        s+=1
        if curr_state=='S':
            break
        elif curr_state=='|':
            if direction=='N':
                curr_state,direction,row,column=check_direction(row,column,l,"TOP")
            else:
                curr_state,direction,row,column=check_direction(row,column,l,"BOT")
        elif curr_state=='-':
            if direction=='E':
                curr_state,direction,row,column=check_direction(row,column,l,"RIGHT")
            else:
                curr_state,direction,row,column=check_direction(row,column,l,"LEFT")
        elif curr_state=='L':
            if direction=='N':
                curr_state,direction,row,column=check_direction(row,column,l,"TOP")
            else:
                curr_state,direction,row,column=check_direction(row,column,l,"RIGHT")
        elif curr_state=='J':
            if direction=='N':
                curr_state,direction,row,column=check_direction(row,column,l,"TOP")
            else:
                curr_state,direction,row,column=check_direction(row,column,l,"LEFT")
        elif curr_state=='7':
            if direction=='W':
                curr_state,direction,row,column=check_direction(row,column,l,"LEFT")
            else:
                curr_state,direction,row,column=check_direction(row,column,l,"BOT")
        elif curr_state=='F':
            if direction=='E':
                curr_state,direction,row,column=check_direction(row,column,l,"RIGHT")
            else:
                curr_state,direction,row,column=check_direction(row,column,l,"BOT")
        
    print(s//2)
    