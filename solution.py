def solution(n: int, x, y):
    list = [x, y, ]
    for i in range(2, n):
        tmp = list[i - 1] + list[i - 2]
        list.append(tmp)
    return list[-1]


if __name__ == '__main__':
    num = solution(10, 1, 2)
    print(num)
