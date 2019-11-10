# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'


def binary_search(arr: list, value) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return -(low + 1)  # 未找到返回-插入点-1


# 2分查找第一个值等于给定值的元素
def bsearch_first(arr: list, value: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] < value:
            low = mid + 1
        elif arr[mid] > value:
            high = mid - 1
        else:
            if mid == 0 or arr[mid - 1] != value:
                return mid
            else:
                high = mid - 1
    return -1


def bsearch_first_simple(arr: list, value: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] >= value:
            high = mid - 1
        else:
            low = mid + 1
    if low < len(arr) and arr[low] == value:
        return low
    else:
        return -1


# 查找最后一个值等于给定值的元素
def bsearch_last(arr: list, value: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] < value:
            low = mid + 1
        elif arr[mid] > value:
            high = mid - 1
        else:
            if mid == 0 or arr[mid + 1] != value:
                return mid
            else:
                low = mid + 1
    return -1


# 查找最后一个值等于给定值的元素
def bsearch_last_simple(arr: list, value: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] <= value:
            low = mid + 1
        else:
            high = mid - 1
    if high >= 0 and arr[high] == value:
        return high
    else:
        return -1


# 查找第一个大于等于给定值的元素
def bsearch_first_not_less(arr: list, value: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] < value:
            low = mid + 1
        else:
            if mid == 0 or arr[mid - 1] < value:
                return mid
            else:
                high = mid - 1
    return -1


# 查找第一个大于等于给定值的元素
def bsearch_first_not_less_simple(arr: list, value: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] >= value:
            high = mid - 1
        else:
            low = mid + 1
    if low < len(arr) and arr[low] >= value:
        return low
    else:
        return -1


# 查找最后一个小于等于给定值的元素
def bsearch_last_not_greater(arr: list, value: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] <= value:
            if mid == len(arr) - 1 or arr[mid + 1] != value:
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1
    return -1


# 查找最后一个小于等于给定值的元素
def bsearch_last_not_greater_simple(arr: list, value: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] <= value:
            low = mid + 1
        else:
            high = mid - 1
    if high >= 0 or arr[high] <= value:
        return high
    else:
        return -1


if __name__ == "__main__":
    arr = [1, 3, 4, 5, 6, 8, 8, 8, 11, 18]
    s = bsearch_last_not_greater(arr, 8)
    print(s)
    s = bsearch_last_not_greater_simple(arr, 8)
    print(s)
    for a in [0, 2, 4, 7]:
        search = binary_search(arr, a)
        if search < 0: search = -(search + 1)
        print(search, end=",")
