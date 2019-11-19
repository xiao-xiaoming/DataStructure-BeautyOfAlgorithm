# 各部分的必知必会&LeetCode练习题

## 1.数组和链表

**关于数组和链表的几个必知必会的代码实现**

**数组：**

- 实现一个支持动态扩容的数组
- 实现一个大小固定的有序数组，支持动态增删改操作
- 实现两个有序数组合并为一个有序数组

**链表：**

- 实现单链表、循环链表、双向链表，支持增删操作
- 实现单链表反转
- 实现两个有序的链表合并为一个有序链表
- 实现求链表的中间结点

**对应的 LeetCode 练习题**

**数组：**

Three Sum（求三数之和）

https://leetcode-cn.com/problems/3sum/

Majority Element（求众数）

https://leetcode-cn.com/problems/majority-element/

Missing Positive（求缺失的第一个正数）

https://leetcode-cn.com/problems/first-missing-positive/

**链表：**

Linked List CycleI（环形链表）

https://leetcode-cn.com/problems/linked-list-cycle/

Merge k Sorted Lists（合并k个排序链表）

https://leetcode-cn.com/problems/merge-k-sorted-lists/

## 2.栈、队列和递归

**关于栈、队列和递归的几个必知必会的代码实现**

**栈：**

- 用数组实现一个顺序栈
- 用链表实现一个链式栈
- 编程模拟实现一个浏览器的前进、后退功能

**队列：**

- 用数组实现一个顺序队列
- 用链表实现一个链式队列
- 实现一个循环队列

**递归：**

- 编程实现斐波那契数列求值 f(n)=f(n-1)+f(n-2)
- 编程实现求阶乘 n!
- 编程实现一组数据集合的全排列

**对应的 LeetCode 练习题**

**栈：**

Valid Parentheses（有效的括号）

https://leetcode-cn.com/problems/valid-parentheses/

Longest Valid Parentheses（最长有效的括号）

https://leetcode-cn.com/problems/longest-valid-parentheses/

Evaluate Reverse Polish Notatio（逆波兰表达式求值）

https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/

**队列：**

Design Circular Deque（设计一个双端队列）

https://leetcode-cn.com/problems/design-circular-deque/

Sliding Window Maximum（滑动窗口最大值）

https://leetcode-cn.com/problems/sliding-window-maximum/

**递归：**

Climbing Stairs（爬楼梯）

https://leetcode-cn.com/problems/climbing-stairs/

## 3.排序和二分查找

**关于排序和二分查找的几个必知必会的代码实现**

排序：

- 实现归并排序、快速排序、插入排序、冒泡排序、选择排序
- 编程实现 O(n) 时间复杂度内找到一组数据的第 K 大元素

二分查找：

- 实现一个有序数组的二分查找算法
- 实现模糊二分查找算法（比如大于等于给定值的第一个元素）

**对应的 LeetCode 练习题**

Sqrt(x) （x 的平方根）

https://leetcode-cn.com/problems/sqrtx/

## 4.散列表和字符串

**关于散列表和字符串的 4 个必知必会的代码实现**

散列表:

- 实现一个基于链表法解决冲突问题的散列表
- 实现一个 LRU 缓存淘汰算法

字符串:

- 实现一个字符集，只包含 a～z 这 26 个英文字母的 Trie 树
- 实现朴素的字符串匹配算法

**对应的LeetCode练习题**

字符串

- Reverse String （反转字符串）

https://leetcode-cn.com/problems/reverse-string/

- Reverse Words in a String（翻转字符串里的单词）

https://leetcode-cn.com/problems/reverse-words-in-a-string/

- String to Integer (atoi)（字符串转换整数 (atoi)）

https://leetcode-cn.com/problems/string-to-integer-atoi/

## 5.二叉树和堆

**关于二叉树和堆的 7 个必知必会的代码实现**

二叉树

- 实现一个二叉查找树，并且支持插入、删除、查找操作
- 实现查找二叉查找树中某个节点的后继、前驱节点
- 实现二叉树前、中、后序以及按层遍历

堆

- 实现一个小顶堆、大顶堆、优先级队列
- 实现堆排序
- 利用优先级队列合并 K 个有序数组
- 求一组动态数据集合的最大 Top K

**对应的 LeetCode 练习题**

- Invert Binary Tree（翻转二叉树）

https://leetcode-cn.com/problems/invert-binary-tree/

- Maximum Depth of Binary Tree（二叉树的最大深度）

https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

- Validate Binary Search Tree（验证二叉查找树）

https://leetcode-cn.com/problems/validate-binary-search-tree/

- Path Sum（路径总和）

https://leetcode-cn.com/problems/path-sum/

## 6.图

**关于图的几个必知必会的代码实现**

图

- 实现有向图、无向图、有权图、无权图的邻接矩阵和邻接表表示方法
- 实现图的深度优先搜索、广度优先搜索
- 实现 Dijkstra 算法、A* 算法
- 实现拓扑排序的 Kahn 算法、DFS 算法

**对应的 LeetCode 练习题**

- Number of Islands（岛屿的个数）

https://leetcode-cn.com/problems/number-of-islands/description/

- Valid Sudoku（有效的数独）

https://leetcode-cn.com/problems/valid-sudoku/

## 7.贪心、分治、回溯和动态规划

**几种算法思想必知必会的代码实现**

回溯

- 利用回溯算法求解八皇后问题
- 利用回溯算法求解 0-1 背包问题

分治

- 利用分治算法求一组数据的逆序对个数

动态规划

- 0-1 背包问题
- 最小路径和（详细可看 @Smallfly 整理的 Minimum Path Sum）
- 编程实现莱文斯坦最短编辑距离
- 编程实现查找两个字符串的最长公共子序列
- 编程实现一个数据序列的最长递增子序列

**对应的 LeetCode 练习题**

- Regular Expression Matching（正则表达式匹配）

https://leetcode-cn.com/problems/regular-expression-matching/

- Minimum Path Sum（最小路径和）

https://leetcode-cn.com/problems/minimum-path-sum/

- Coin Change （零钱兑换）

https://leetcode-cn.com/problems/coin-change/

- Best Time to Buy and Sell Stock（买卖股票的最佳时机）

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

- Maximum Product Subarray（乘积最大子序列）

https://leetcode-cn.com/problems/maximum-product-subarray/

- Triangle（三角形最小路径和）

https://leetcode-cn.com/problems/triangle/





## 测试题

电商交易系统中，订单数据一般都会很大，一般都会分库分表来存储。假设分了 10 个库并存储在不同的机器上，在不引入复杂的分库分表中间件的情况下，希望开发一个小的功能，能够快速地查询金额最大的前 K 个订单（K 是输入参数，可能是 1、10、1000、10000，假设最大不会超过 10 万）。

背景：

- 数据库中，订单表的金额字段上建有索引，可以通过 select order by limit 语句来获取数据库中的数据；
- 机器的可用内存有限，比如只有几百 M 剩余可用内存。需要尽量节省内存，不要发生 Out of Memory Error。

**如何设计这样一个系统呢？**

**解析**

维护一个 K 大小的小顶堆，将要求Top K的数据逐个取出与堆顶的元素对比，如果元素比堆顶元素大就把堆顶元素删除，并且将这个元素插入到堆中；如果比堆顶元素小，则不做处理。

从第一个数据库开始通过select order by limit语句读取前 K 个订单数据，插入到小顶堆中，再从第2个数据库读取前 K 个订单数据插入到小顶堆，直到读完10个库，每个库都返回自己数据库内部局部的金额最大的前 K 个订单，最终大顶堆中的数据就是全局金额最大的前K个订单。

假设一条订单平均1KB大小，用于计算金额前k大的订单是机器使用100MB计算该任务，即使要快速地查询金额最大的前10万个订单，维护一个大小为10万的大顶堆，内存也是够用的。

如果数据库一次性返回k个数据，数据量太大SQL 执行很慢，那就需要分批执行SQL，根据实际情况判断数据库每次返回的数据个数。



