# coding=utf-8
__author__ = 'xiaoxiaoming'


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# 输出了第10个斐波那契数列
print("斐波那契数列：")
for i in range(10):
    print(fib(i), end=",")
