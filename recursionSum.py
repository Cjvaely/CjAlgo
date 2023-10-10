def sum(arr):
    """算法图解4.1 递归函数计算列表中元素的总和"""
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])


def numOfElements(arr):
    """算法图解4.2 递归函数来计算列表包含的元素数"""
    if len(arr) == 0:
        return 0
    else:
        return (1 + numOfElements(arr[1:]))


def findMaxNum(arr):
    """算法图解4.3 递归函数来找出列表最大数"""
    if len(arr) == 1:
        return arr[0]
    elif len(arr) > 1:
        return arr[0] if arr[0] >= findMaxNum(arr[1:]) else findMaxNum(arr[1:])


def main():
    print(sum([88, 8, 3, 4, 6, 9]))
    print(numOfElements([88, 8, 3, 4, 6, 9]))
    print(findMaxNum([88, 8, 89, 102, 97]))

if __name__ == '__main__':
    main()