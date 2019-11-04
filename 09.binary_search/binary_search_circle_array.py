# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'


def binary_search_circle_array(arr: list, value) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) >> 1
        if arr[mid] == value: return mid
        # 上面没有返回，说明中间值不是目标值
        if arr[mid] < arr[high]:  # 若中间数小于最右边数，则右半段是升序区间
            if arr[mid] < value and value <= arr[high]:  # 在右半段有序区间
                low = mid + 1
            else:
                high = mid - 1
        elif arr[mid] > arr[high]:  # 若中间数大于最右边数，则左半段是升序区间
            if arr[low] <= value and value < arr[mid]:  # 在左半段有序区间
                high = mid - 1
            else:
                low = mid + 1
        else:  # 若中间数等于最右边数，则目标不在右半段
            high = mid - 1
    return -1


for i in range(0, 9):
    v = binary_search_circle_array([4, 5, 6, 1, 2, 3], i)
    print(v)
