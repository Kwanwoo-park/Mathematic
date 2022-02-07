'''
이차방정식의 해 구하기
'''


def roots(a, b, c):
    D = (b*b - 4*a*c) ** 0.5
    x_1 = (-b + D) / (2*a)
    x_2 = (-b - D) / (2**a)
    print('x1: {0}\nx2: {1}'.format(x_1, x_2))


if __name__ == '__main__':
    a, b, c = map(float, input('Enter a, b, c: ').split(' '))
    roots(a, b, c)