#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Pattern:
    def __init__(self, regex: str):
        self.regex = regex  # 正则表达式
        self.matched = False

    def rmatch(self, r_idx: int, m_idx: int, main: str):
        if self.matched: return  # 如果已经匹配了，就不要继续递归了
        if r_idx == len(self.regex):  # 正则表达式到结尾了
            if m_idx == len(main): self.matched = True  # 文本串也到结尾了
            return
        if self.regex[r_idx] == '*':  # *匹配1个或多个任意字符
            for i in range(m_idx, len(main)):
                self.rmatch(r_idx + 1, i + 1, main)
        elif self.regex[r_idx] == '?':  # ? 匹配0个或者1个字符
            self.rmatch(r_idx + 1, m_idx, main)
            self.rmatch(r_idx + 1, m_idx + 1, main)
        elif m_idx < len(main) and self.regex[r_idx] == main[m_idx]:  # 非特殊字符需要精确匹配
            self.rmatch(r_idx + 1, m_idx + 1, main)

    def match(self, main):
        self.matched = False
        self.rmatch(0, 0, main)
        return self.matched



if __name__ == '__main__':
    regex = 'ab*eee?d'
    main = 'abcdsadfkjlekjoiwjiojieeecd'
    pattern = Pattern(regex)
    match = pattern.match(main)
    print(match)
