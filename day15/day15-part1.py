def get_hash_sum(s):
    curr=0
    for i in s:
        curr=((curr+ord(i))*17)%256
    return curr
if __name__=='__main__':
    s=0
    with open(file='sample_input.txt') as f:
        lines=f.readlines()
    for i in lines[0].split(','):
        s+=get_hash_sum(i)
    print(s)
