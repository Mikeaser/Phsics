import numpy as np
import math

#  圆的半径r=1


def Cauculate(n):
    # 边长对应的圆心角
    theta = 2*math.pi/n
    # 内接多边形与外界多边形面积
    S_in = 0.5*math.sin(theta)*n
    S_out = math.tan(theta/2)*n
    delta = S_out - S_in
    return S_in, S_out, delta


if __name__ == '__main__':
    n = 6
    while True:
        S_in, S_out, delta = Cauculate(n)
        if delta < 1e-12:
            break
        n += 1
    print("pi = ", S_in)
