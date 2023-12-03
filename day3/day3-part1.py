import re
import numpy as np

suma=0
def check_adjencet(array,i,j):
    global suma
    for k in range(i-1,i+2):
        for l in range(j-1,j+2):
            #print(array[k][l])
            if array[k][l].isdigit():
                m=l
                s=''
                while array[k][m].isdigit():
                    m-=1
                m+=1
                while array[k][m].isdigit():
                    s+=array[k][m]
                    array[k][m]='.'
                    m+=1
                number=int(s)
                #print(number)
                suma+=number

if __name__=='__main__':
    array=[]
    with open(file='input.txt') as f:
        lines=f.readlines()

    l=[]
    for i in lines:
        l=list(i[:-1])
        array.append(['.']+l+['.'])
    cols=len(l)+2  
    rows=len(array)+2
    array=[['.' for i in range(cols)]]+array
    array.append(['.' for i in range(cols)])
    #print(array)
    for i in range(1,rows-1):
        for j in range(1,cols-1):        
            if array[i][j]!='.' and not array[i][j].isdigit():
                check_adjencet(array,i,j)
        
    print(suma)