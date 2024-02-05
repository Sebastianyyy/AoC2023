from sympy import solve_poly_system, Symbol


class Hailstone:
    def __init__(self, point_x, point_y, point_z, velocity_x, velocity_y, velocity_z):
        self.point_x = point_x
        self.velocity_x = velocity_x
        self.point_y = point_y
        self.velocity_y = velocity_y
        self.point_z = point_z
        self.velocity_z = velocity_z


if __name__ == '__main__':
    with open(file='input.txt') as f:
        lines = f.readlines()
    array = []
    for i in lines:
        points, velocities = i.split('@')
        points = list(map(int, points.split(',')))
        velocities = list(map(int, velocities.split(',')))
        array.append(Hailstone(*points, *velocities))
    s = 0
    x_start = Symbol('x_start')
    y_start = Symbol('y_start')
    z_start = Symbol('z_start')
    xv_start = Symbol('xv_start')
    yv_start = Symbol('yv_start')
    zv_start = Symbol('zv_start')
    equations = []
    t_syms = []

    for idx, hailstone in enumerate(array[:3]):
        x, y, z, xv, yv, zv = hailstone.point_x, hailstone.point_y, hailstone.point_z, hailstone.velocity_x, hailstone.velocity_y, hailstone.velocity_z
        t = Symbol('t'+str(idx))
        eqx = x_start+xv_start*t-x-xv*t
        eqy = y_start+yv_start*t-y-yv*t
        eqz = z_start+zv_start*t-z-zv*t
        equations.append(eqx)
        equations.append(eqy)
        equations.append(eqz)
        t_syms.append(t)

    result = solve_poly_system(
        equations, *([x_start, y_start, z_start, xv_start, yv_start, zv_start]+t_syms))

    print(int(result[0][0]+result[0][1]+result[0][2]))
