#请你写一个堆排序
def heapify(arr, n, i):
    largest = i  # 初始化最大值为根节点
    left = 2 * i + 1  # 左子节点索引
    right = 2 * i + 2  # 右子节点索引

    # 如果左子节点比根节点大
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 如果右子节点比当前最大值大
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大值不是根节点，交换并继续堆化
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # 构建最大堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 一个个从堆中取出元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)  # 重新堆化


if __name__ == '__main__':
    data = [12, 11, 13, 5, 6, 7]
    print("原始数组:", data)
    heapSort(data)
    print("排序后数组:", data)
    # tree.add(i)
    # print("前序遍历结果:")