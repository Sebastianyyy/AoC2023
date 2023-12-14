import numpy as np

def count_of_circles(array):
    c=array.shape[0]
    s=0
    print(array)
    for idx,i in enumerate(range(c,0,-1)):
        s+=((array[idx,:]=='O').sum())*i
    return s
def gravitation_rows_to_left(array):
    print(array)
    idx_of_h=np.argwhere(array=='#')
    for i,j in zip(range(idx_of_h.shape[0]-1),range(1,idx_of_h.shape[0])):
        if idx_of_h[i,1]==array.shape[1]-1:
            continue
        number_of_hasthags=array[idx_of_h[i,:][0],idx_of_h[i,:][1]+1:idx_of_h[j,:][1]]
        number_of_hasthags=np.sort(number_of_hasthags)[::-1]
        array[idx_of_h[i,:][0],idx_of_h[i,:][1]+1:idx_of_h[j,:][1]]=number_of_hasthags
    return count_of_circles(array.T[1:-1,:])
if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    t=[['#']*(len(lines[0])-1)]
    s=0
    for i in (lines):
        t.append(list(i[:-1]))
    t.append(["#"]*(len(lines[0])-1))
    
    array=(np.vstack([k for k in t]))
    print(gravitation_rows_to_left(array.T))