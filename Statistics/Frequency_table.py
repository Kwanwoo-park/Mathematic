from collections import Counter
'''
여러 숫자 리스트에 대한 빈도 테이블
'''


def frequency_table(numbers):
    table = Counter(numbers)
    print('Number\tFrequency')

    for number in sorted(table.most_common()):
        print('{0}\t{1}'.format(number[0], number[1]))


if __name__ == '__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    frequency_table(scores)