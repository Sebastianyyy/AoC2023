opportunities={"N":(-1,0),"S":(1,0),"W":(0,-1),"E":(0,1)}

def valid(r,c,row,column,array):
    if r>=0 and r<row and c>=0 and c<column and array[r][c]=='.':
        return True
    return False

if __name__=='__main__':
    s=0
    with open(file='input.txt') as f:
        lines=f.readlines()
    #print(lines)
    array=[list(i[:-1]) for i in lines]
    row,col=0,0
    array_rows=len(array)
    array_cols=len(array[0])
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]=='S':
                row,col=i,j
    array[row][col]='.'
    plots={(row,col)}
    m=0
    for i in range(64):
        plots2=set()
        for r,c in plots:
            for dir in opportunities:
                if valid(r+opportunities[dir][0],c+opportunities[dir][1],array_rows,array_cols,array):
                    plots2.add((r+opportunities[dir][0],c+opportunities[dir][1]))
        
        plots=plots2
    print(len(plots2))

