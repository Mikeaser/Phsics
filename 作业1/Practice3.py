# 光的衍射现象的模拟

import matplotlib.pyplot as plt
import math
import numpy as np


def Diffraction(a, d, lam, N):
    theta = np.arange(-math.pi/2, math.pi/2, 1e-4).tolist()
    I_list = []
    for i in range(len(theta)):
        u = math.pi*a*math.sin(theta[i])/lam
        v = math.pi*d*math.sin(theta[i])/lam
        I = ((math.sin(u)/u)*(math.sin(N*v)/v))**2
        I_list.append(I)
    return theta, I_list


if __name__ == "__main__":
    a = 650
    d = 700
    lam = 460
    N = 5
    theta, I = Diffraction(a, d, lam, N)
    plt.plot(theta, I)
    plt.savefig('./作业1/result.jpg')

# 可以看到结果的图片中有一段衍射主极大对应的尖峰
# 并且周围有逐渐递减的次极大
