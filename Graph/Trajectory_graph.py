import math
from matplotlib import pyplot as plt
'''
공중에 투척한 물체의 포물선 궤적 그리기
'''


def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')


def frange(start, fianl, interval):
    numbers = []
    while start < fianl:
        numbers.append(start)
        start += interval

    return numbers


def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8

    t_flight = 2*u*math.sin(theta)/g

    interval = frange(0, t_flight, 0.001)

    x = []
    y = []

    for t in interval:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)

    draw_graph(x, y)


if __name__ == '__main__':
    # try:
    #     u = float(input('Enter the initial velocity (m/s): '))
    #     theta = float(input('Enter the angle of projection (degrees): '))
    # except:
    #     print('You entered an invalid input')
    # else:
    #     draw_trajectory(u, theta)
    #     plt.show()
    u_list = [20, 40, 60]
    theta_list = [30, 45, 60]

    for u, theta in zip(u_list, theta_list):
        draw_trajectory(u, theta)

    plt.legend(['20', '40', '60'])
    plt.show()