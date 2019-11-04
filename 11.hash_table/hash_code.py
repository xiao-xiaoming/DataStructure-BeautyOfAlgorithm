# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'


def hash_code(s: str) -> int:
    result = 0
    base = ord('a')
    for ch in s.lower():
        result = result * 26 + (ord(ch) - base)
    return result


print(hash_code("abc"))
