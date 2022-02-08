import matplotlib.pyplot as plt
import random
'''
두 개의 동일한 확률의 가능성 변환으로부터 변환을 선택하는 예제
'''


def transformation_1(p):
    x = p[0]
    y = p[1]
    return x+1, y-1


def transformation_2(p):
    x = p[0]
    y = p[1]
    return x+1, y+1


def transform(p):
    transformation = [transformation_1(p), transformation_2(p)]
    t = random.choice(transformation)
    x, y = t
    return x, y


def build_trajectory(p, n):
    x = [p[0]]
    y = [p[1]]

    for i in range(n):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])

    return x, y


p = (1, 1)
n = int(input('Enter the number of iterations: '))
x, y = build_trajectory(p, n)
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()