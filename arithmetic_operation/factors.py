'''
정수 팩터를 계산한다.
'''


def factors(b):
    for i in range(1,b+1):
        if b % i == 0:
            print(i)


if __name__ == '__main__':
    b = float(input('Your Number Please'))
    if b > 0 and b.is_integer():
        factors(int(b))
    else:
        print('Please enter a positive integer')