import re
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
directions={"R":(0,1),"L":(0,-1),"U":(-1,0),"D":(1,0)}
def polygonArea(vertices):
  numberOfVertices = len(vertices)
  sum1 = 0
  sum2 = 0
  for i in range(0,numberOfVertices-1):
    sum1 = sum1 + vertices[i].x *  vertices[i+1].y
    sum2 = sum2 + vertices[i].y *  vertices[i+1].x
  sum1 = sum1 + vertices[numberOfVertices-1].x*vertices[0].y
  sum2 = sum2 + vertices[0].x*vertices[numberOfVertices-1].y
  area = abs(sum1 - sum2) / 2
  return area

if __name__=='__main__':
    s=0
    with open(file='sample_input.txt') as f:
        lines=f.readlines()
    array=[]
    curr_x,curr_y,value,b=0,0,0,0
    for i in lines:
        value=int(re.match(pattern=r'. (\d+)',string=i[:-1]).group(1))
        b+=value
        curr_x,curr_y=curr_x+directions[i[0]][0]*value,curr_y+directions[i[0]][1]*value
        array.append(Point(curr_x,curr_y))
    array=array[::-1]
    for i in array:
        print(i.x,i.y)
    print(polygonArea(array)+b//2+1)
    print()