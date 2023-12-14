import numpy as np

def rows_mirror(array):
    for i in range(1,array.shape[0]//2+1):
        first=array[:i,:]
        second=array[i:2*i,:]
        if np.array_equal(first,second[::-1,:]):
            print(i)
            return i
    for i in range(array.shape[0]//2+1,array.shape[0]):
        j=i-(array.shape[0]-i)
        first=array[i:,:]
        second=array[j:i,:]
        if np.array_equal(first,second[::-1,:]):
            print(i)
            return i
    
    return 0
def cols_mirror(array):
    for i in range(1,array.shape[1]//2+1):
        first=array[:,:i]
        second=array[:,i:2*i]
        if np.array_equal(first,second[:,::-1]):
            print(i)
            return i
    for i in range(array.shape[1]//2+1,array.shape[1]):
        j=i-(array.shape[1]-i)
        first=array[:,i:]
        second=array[:,j:i]
        if np.array_equal(first,second[:,::-1]):
            print(i)

            return i
    return 0

if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    t=[]
    s=0
    for i in (lines):
        if i!='\n':
            t.append(list(i[:-1]))
        else:
            array=(np.vstack([k for k in t]))
            t=[]
            s+=rows_mirror(array)*100
            s+=cols_mirror(array)
    print(s)