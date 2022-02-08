import matplotlib.pyplot as plt
'''
matplotlib의 circle 패치를 사용한 예제
'''


def create_circle():
    circle = plt.Circle((0, 0), radius=0.5)
    return circle


def show_shape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    ax.set_aspect('equal')
    plt.axis('scaled')
    plt.show()


c = create_circle()
show_shape(c)