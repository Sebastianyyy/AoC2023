import numpy as np

def count_of_circles(array):
    c=array.shape[0]
    s=0
    print(array)
    for idx,i in enumerate(range(c,0,-1)):
        s+=((array[idx,:]=='O').sum())*i
    return s
def gravitation_rows_to_left(array):
    idx_of_h=np.argwhere(array=='#')
    for i,j in zip(range(idx_of_h.shape[0]-1),range(1,idx_of_h.shape[0])):
        if idx_of_h[i,1]==array.shape[1]-1:
            continue
        number_of_hasthags=array[idx_of_h[i,:][0],idx_of_h[i,:][1]+1:idx_of_h[j,:][1]]
        number_of_hasthags=np.sort(number_of_hasthags)[::-1]
        array[idx_of_h[i,:][0],idx_of_h[i,:][1]+1:idx_of_h[j,:][1]]=number_of_hasthags
    return array
if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    t=[['#']*(len(lines[0])+1)]
    s=0
    for i in (lines):
        t.append(list('#'+i[:-1]+'#'))
    t.append(["#"]*(len(lines[0])+1))
    array=(np.vstack([k for k in t]))
    array2=array.copy()
    arrays=[]
    found_id=0
    for i in range(1,1000000000):
        array=gravitation_rows_to_left(array.T).T
        array=gravitation_rows_to_left(array)
        array=gravitation_rows_to_left(array.T[:,::-1])[:,::-1].T
        array=gravitation_rows_to_left(array[:,::-1])[:,::-1]
        found=False
        found_id=i
        for id,j in enumerate(arrays,1):
            if np.array_equal(array,j):
                found=True
                len_of_cycle=i-id  
        arrays.append(array.copy())
        if found:
            break
    for i in range((1000000000-found_id)%len_of_cycle):
        array=gravitation_rows_to_left(array.T).T
        array=gravitation_rows_to_left(array)
        array=gravitation_rows_to_left(array.T[:,::-1])[:,::-1].T
        array=gravitation_rows_to_left(array[:,::-1])[:,::-1]
    print(count_of_circles(array[1:-1,:]))