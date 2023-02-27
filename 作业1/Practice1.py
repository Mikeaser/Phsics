# 第一题，利用割圆法周长逼近求解pi

import math


if __name__ == "__main__":
    #  圆的半径
    r = 0.5
    l_in = r  # 从六边形开始，内接边长即为半径
    k = 6
    while True:
        h = math.sqrt(r**2-(l_in/2)**2)
        delta = r-h
        l_in = math.sqrt((l_in/2)**2+delta**2)
        k *= 2
        pi_min = k * l_in
        theta = math.asin(l_in/(2*r))   # 通过内接多边形边长计算外切边长
        l_out = 2*r*math.tan(theta)
        pi_max = k * l_out
        pi = (pi_max + pi_min)/2
        if abs(pi-math.pi)< 1e-12:
            print("截止为正%d边形" %k)
            print("pi的下限为%.13f" %pi_min)
            print("pi的上限为%.13f" %pi_max)
            print("pi的近似值为%.12f" %pi)
            break
