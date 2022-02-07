import matplotlib.pyplot as plt
'''
숫자 리스트에 대한 분산과 표준편차
'''


def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)

    mean = s/N

    return mean


def find_differences(numbers):
    mean = calculate_mean(numbers)
    diff = []

    for num in numbers:
        diff.append(num-mean)

    return mean, diff


def calculate_variance(numbers):
    mean, diff = find_differences(numbers)

    squared_diff = []

    for d in diff:
        squared_diff.append(d**2)

    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(numbers)
    return mean, variance


if __name__ == '__main__':
    months = range(1, 13)
    donations1 = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    mean1, variance1 = calculate_variance(donations1)
    std1 = variance1**0.5
    print('Average is {0}, variance is {1}, standard deviation is {2}'.format(mean1, variance1, std1))

    donations2 = [382, 389, 377, 397, 396, 368, 369, 392, 398, 367, 393, 396]
    mean2, variance2 = calculate_variance(donations2)
    std2 = variance2**0.5
    print('Average is {0}, variance is {1}, standard deviation is {2}'.format(mean2, variance2, std2))

    plt.plot(months, donations1, marker='o')
    plt.hlines(mean1, -1, 12)
    plt.plot(months, donations2, marker='o')
    plt.hlines(mean2, -1, 12)
    plt.title('Average donation')
    plt.xlabel('donation')
    plt.ylabel('months')
    plt.legend(['donation1', 'donation2', 'mean1', 'mean2'])
    plt.show()