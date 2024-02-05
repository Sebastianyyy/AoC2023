from sympy import solve
from sympy.abc import x, y


class Hailstone:
    def __init__(self, point_x, point_y, velocity_x, velocity_y):
        self.point_x = point_x
        self.velocity_x = velocity_x
        self.point_y = point_y
        self.velocity_y = velocity_y


if __name__ == '__main__':
    with open(file='input.txt') as f:
        lines = f.readlines()
    array = []
    for i in lines:
        points, velocities = i.split('@')
        # print(points,velocities)
        points = list(map(int, points.split(',')[:-1]))
        velocities = list(map(int, velocities.split(',')[:-1]))
        array.append(Hailstone(*points, *velocities))
    
    s = 0
    start = 200000000000000
    end = 400000000000000
    seen_a=set()
    seen_b=set()
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            print(i,j)
            #print(array[i].point_x, array[i].point_y,
            #      array[j].point_x, array[j].point_y)
            equation_f = f"{array[i].point_x}+({array[i].velocity_x})*x+{-array[j].point_x}+({-array[j].velocity_x})*y"
            equation_s = f"{array[i].point_y}+({array[i].velocity_y})*x+{-array[j].point_y}+({-array[j].velocity_y})*y"
            #print(equation_f,equation_s)
            sol = solve([eval(equation_f), eval(equation_s)], x, y, dict=True)
            #print(sol)
            if len(sol) != 0:
               # print("XD")
                a, b = sol[0][x], sol[0][y]
                #if a in seen_a or b in seen_b:
                #    continue
                #print(a,b)
                seen_a.add(a)
                seen_b.add(b)
                #print(a, b)
                if a<0 or b<0:
                    continue
                a_ = array[i].point_x+array[i].velocity_x*float(a)
                b_ = array[j].point_y+array[j].velocity_y*float(b)
                #print(a_,b_)
                if start<=a_<=end and start<=b_<=end:
                    s+=1
    print(s)
