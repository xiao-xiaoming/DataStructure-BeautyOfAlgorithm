# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

arr1 = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
arr2 = ['apple', 'apple', 'pear', 'banana', 'Apricot','Avocado']
common_str = set(arr1) & set(arr2)
print(common_str)

