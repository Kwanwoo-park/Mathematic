import math
from sympy import Derivative, Symbol, sin
'''
그레디언트 상승을 이용해 투척각도를 계산한다.
'''


def grad_ascent(x0, flx, x):
    epsilon = 1e-6
    step_size = 1e-4
    x_old = x0
    x_new = x_old + step_size*flx.subs({x: x_old}).evalf()

    while abs(x_old - x_new) > epsilon:
        x_old = x_new
        x_new = x_old + step_size*flx.subs({x:x_old}).evalf()

    return x_new


def find_max_theta(R, theta):
    R1theta = Derivative(R, theta).doit()
    theta0 = 1e-3
    theta_max = grad_ascent(theta0, R1theta, theta)
    return theta_max


if __name__ == '__main__':
    g = 9.8
    u = 25
    theta = Symbol('theta')
    R = u**2*sin(2*theta)/g

    theta_max = find_max_theta(R, theta)
    print('Theta: {0}'.format(math.degrees(theta_max)))
    print('Maximum Range: {0}'.format(R.subs({theta:theta_max})))