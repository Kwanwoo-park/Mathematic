from sympy import expand, sympify, pprint
from sympy.core.sympify import SympifyError
'''
두 수식의 곱
'''


def product(expr1, expr2):
    prod = expand(expr1*expr2)
    pprint(prod)


if __name__ == '__main__':
    expr1 = input('Enter the first expression: ')
    expr2 = input('Enter the second expression: ')

    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print('Invalid input')
    else:
        product(expr1, expr2)