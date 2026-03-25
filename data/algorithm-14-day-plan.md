---
title: 14天算法学习
date: 2026-03-25
summary: 学习算法准备面试
---
# 14-Day Algorithm Interview Plan

目标：先拿下高频 `Easy/Medium`，建立稳定的题型识别和代码输出能力。

原则：
- 每天做 `3` 题：`2` 道新题 + `1` 道复写题
- 每道题都要说出：思路、复杂度、边界条件
- 新题控制在 `25-35` 分钟内，复写题控制在 `10-15` 分钟内
- 做完当天题目后，整理 `3` 行复盘：题型信号、核心技巧、易错点

## Day 1: 数组 + 哈希

- `1. Two Sum`
- `49. Group Anagrams`
- `128. Longest Consecutive Sequence`

可加练（推荐顺序）：
- `217. Contains Duplicate`
- `242. Valid Anagram`
- `219. Contains Duplicate II`
- `205. Isomorphic Strings`
- `350. Intersection of Two Arrays II`
- `36. Valid Sudoku`
- `454. 4Sum II`
- `560. Subarray Sum Equals K`

复写：
- `1. Two Sum`

目标：
- 熟悉哈希表判重、计数、映射三种基本用法

## Day 2: 双指针

- `11. Container With Most Water`
- `15. 3Sum`
- `283. Move Zeroes`

复写：
- `15. 3Sum`

目标：
- 看到“有序、去重、左右逼近”时能联想到双指针

## Day 3: 滑动窗口

- `3. Longest Substring Without Repeating Characters`
- `438. Find All Anagrams in a String`
- `76. Minimum Window Substring`

复写：
- `3. Longest Substring Without Repeating Characters`

目标：
- 掌握“扩大窗口、收缩窗口、维护计数”的固定套路

## Day 4: 链表

- `206. Reverse Linked List`
- `141. Linked List Cycle`
- `21. Merge Two Sorted Lists`

复写：
- `206. Reverse Linked List`

目标：
- 熟悉链表指针移动，避免断链和空指针

## Day 5: 链表进阶

- `19. Remove Nth Node From End of List`
- `143. Reorder List`
- `23. Merge k Sorted Lists`

复写：
- `19. Remove Nth Node From End of List`

目标：
- 掌握快慢指针、哑节点、链表分段处理

## Day 6: 栈 + 队列

- `20. Valid Parentheses`
- `155. Min Stack`
- `739. Daily Temperatures`

复写：
- `739. Daily Temperatures`

目标：
- 识别单调栈题型，理解“维护递减/递增栈”的意义

## Day 7: 二叉树基础

- `104. Maximum Depth of Binary Tree`
- `102. Binary Tree Level Order Traversal`
- `226. Invert Binary Tree`

复写：
- `102. Binary Tree Level Order Traversal`

目标：
- DFS 和 BFS 两种遍历写法都要熟

## Day 8: 二叉树高频

- `94. Binary Tree Inorder Traversal`
- `236. Lowest Common Ancestor of a Binary Tree`
- `124. Binary Tree Maximum Path Sum`

复写：
- `236. Lowest Common Ancestor of a Binary Tree`

目标：
- 学会递归函数定义，明确“当前节点向上返回什么”

## Day 9: 图搜索

- `200. Number of Islands`
- `695. Max Area of Island`
- `994. Rotting Oranges`

复写：
- `200. Number of Islands`

目标：
- 区分 DFS 染色和 BFS 分层扩散

## Day 10: 二分查找

- `704. Binary Search`
- `35. Search Insert Position`
- `33. Search in Rotated Sorted Array`

复写：
- `33. Search in Rotated Sorted Array`

目标：
- 统一边界写法，避免 `left <= right` 和 `left < right` 混乱

## Day 11: 堆 + Top K

- `215. Kth Largest Element in an Array`
- `347. Top K Frequent Elements`
- `23. Merge k Sorted Lists`

复写：
- `347. Top K Frequent Elements`

目标：
- 看到 “Top K / 第 K 大 / 多路合并” 能立即想到堆

## Day 12: 回溯

- `46. Permutations`
- `78. Subsets`
- `22. Generate Parentheses`

复写：
- `46. Permutations`

目标：
- 固化回溯模板：路径、选择列表、结束条件、撤销选择

## Day 13: 动态规划基础

- `70. Climbing Stairs`
- `198. House Robber`
- `322. Coin Change`

复写：
- `198. House Robber`

目标：
- 先定义状态，再写转移，最后看初始化

## Day 14: 动态规划进阶 + 面试压轴

- `300. Longest Increasing Subsequence`
- `72. Edit Distance`
- `139. Word Break`

复写：
- `72. Edit Distance`

目标：
- 能独立说清二维 DP 的状态定义和转移逻辑

## 每天固定流程

1. 先看题，`5` 分钟内判断题型
2. 不看答案，先说朴素思路和优化方向
3. 手写代码
4. 手动过样例和边界
5. 记录错因

## 复盘模板

- 题号：
- 题型信号：
- 核心解法：
- 易错点：
- 是否需要二刷：

## 最终验收标准

- `1 / 49 / 11 / 15 / 3 / 206 / 19 / 739 / 102 / 236 / 200 / 33 / 347 / 46 / 198 / 72`
  这些题要能脱稿写出来
- 大部分高频 `Medium` 题，`10` 分钟内能定方向
- 常见题型看到关键词就能归类

## 如果你还有时间

第二轮优先补这些题：

- `56. Merge Intervals`
- `146. LRU Cache`
- `148. Sort List`
- `207. Course Schedule`
- `208. Implement Trie`
- `560. Subarray Sum Equals K`
- `221. Maximal Square`
- `416. Partition Equal Subset Sum`
