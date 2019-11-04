# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

"""
    实现游览器的前进后退功能
    解答：使用X 和 Y两个栈，栈 X中的栈顶数据表示当前访问的页面
    访问新页面时把浏览的页面依次压入栈 X，并清空栈Y。
    点击后退按钮时，从栈 X 取出数据放入栈 Y。
    点击前进按钮时，从栈 Y 中取出数据，放入栈 X 中。
    当栈 X 中仅剩1个数据时，说明没有页面可以继续后退浏览了。
    当栈 Y 中没有数据，  说明没有页面可以点击前进按钮浏览了。

"""

from collections import deque


class Browser():

    def __init__(self):
        self.x_stack = deque()
        self.y_stack = deque()

    def can_back(self):
        return len(self.x_stack) > 1

    def can_forward(self):
        return len(self.y_stack) > 0

    def open(self, url):
        print("Open new url %s" % url, end="\n")
        self.x_stack.appendleft(url)
        self.y_stack.clear()

    def back(self):
        if self.can_back():
            self.y_stack.appendleft(self.x_stack.popleft())
            print("back to %s" % self.x_stack[0], end="\n")

    def forward(self):
        if self.can_forward():
            self.x_stack.appendleft(self.y_stack.popleft())
            print("forward to %s" % self.x_stack[0], end="\n")

    def __repr__(self):
        return "X:HEAD=>%s,Y:HEAD=>%s" % ("->".join(self.x_stack) or "None", "->".join(self.y_stack) or "None")

if __name__ == '__main__':
    browser = Browser()
    print("顺序查看了 a，b，c 三个页面")
    browser.open('a')
    browser.open('b')
    browser.open('c')
    print(browser)
    print("点击两次后退按钮")
    browser.back()
    browser.back()
    print(browser)
    print("又点击一次前进按钮")
    browser.forward()
    print(browser)
    print("访问新页面 d")
    browser.open('d')
    print(browser)
