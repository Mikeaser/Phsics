# 使用级数法求解pi

import math

Truepi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# 精度可调
k = 20
auc = 10**(-k)
# n max最大迭代次数，可调
n_max = 1e8

# 数列的第n项，从1开始
def Item(z, n):
    item = (-1)**(n+1)*z**(2*n-1)/(2*n-1)
    return item


if __name__ == "__main__":
    ans = 0
    n = 1
    z = 1/math.sqrt(3)
    while True:
        ans += Item(z, n)
        pi = 6*ans
        n += 1
        if abs(pi - Truepi) < auc:
            break
        if n > n_max:
            print('迭代次数已经达到上限')
            break
    pi = round(pi,k+1)
    print('经过{}次迭代，pi的值为{}'.format(n, pi))


# 讨论：由于每次计算项时都会由于计算机结构造成一部分误差，因此此类收敛
# 过慢的级数不利于精确求解pi。
