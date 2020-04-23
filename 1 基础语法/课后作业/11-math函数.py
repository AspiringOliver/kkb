import math,requests


# def calc(a, b):
#     c = math.ceil(b / 5)
#     print('%.6f公里数，组成了%d组人，需要%d天修完' % (a, c, (math.ceil(a / c))))
#
#
# x = float(input('请输入公里数：\n'))
# y = int(input('请输入人数：\n'))
# calc(x, y)


def weight(a):
    if a <= 5:
        print('运费20元。')
    else:
        b = 20 + 2 * math.ceil(a - 5)
        print('运费%d' % b)


wei = float(input('请输入货重：\n'))
weight(wei)
