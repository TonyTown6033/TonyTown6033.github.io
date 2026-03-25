---
title: Python 数组与哈希速查表
date: 2026-03-25
summary: 刷题必备：list 和 dict 的核心操作、时间复杂度与常用技巧，一页搞定。
---

# Python 数组与哈希速查表

刷题和写业务代码时，list 和 dict 是用得最多的两个结构。这篇速查表把最常用的操作、时间复杂度、以及坑点集中在一起，用的时候直接找对应的部分。

---

## 数组（list）

### 创建

```python
a = []                  # 空数组
a = [0] * 5             # [0, 0, 0, 0, 0]
a = list(range(5))      # [0, 1, 2, 3, 4]
a = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# 二维数组
matrix = [[0] * 3 for _ in range(3)]   # 正确：独立行
matrix = [[0] * 3] * 3                 # 错！三行共享同一对象
```

### 增删改查

| 操作 | 写法 | 时间复杂度 |
|------|------|-----------|
| 末尾追加 | `a.append(x)` | O(1) 均摊 |
| 末尾弹出 | `a.pop()` | O(1) |
| 指定位置插入 | `a.insert(i, x)` | O(n) |
| 指定位置删除 | `a.pop(i)` | O(n) |
| 按值删除 | `a.remove(x)` | O(n) |
| 查找下标 | `a.index(x)` | O(n) |
| 是否存在 | `x in a` | O(n) |
| 取长度 | `len(a)` | O(1) |

```python
a = [1, 2, 3, 4]

a.append(5)       # [1, 2, 3, 4, 5]
a.pop()           # 返回 5，数组变 [1, 2, 3, 4]
a.insert(1, 99)   # [1, 99, 2, 3, 4]
a.pop(1)          # 返回 99，变回 [1, 2, 3, 4]
a.remove(3)       # [1, 2, 4]
```

### 切片

```python
a = [0, 1, 2, 3, 4]

a[1:3]    # [1, 2]        从下标 1 到 2（不含 3）
a[:3]     # [0, 1, 2]     前三个
a[2:]     # [2, 3, 4]     从下标 2 到末尾
a[-2:]    # [3, 4]        最后两个
a[::-1]   # [4, 3, 2, 1, 0]  反转（返回新数组）
a[::2]    # [0, 2, 4]     每隔一个取一个
```

### 排序

```python
a = [3, 1, 4, 1, 5]

a.sort()                    # 原地排序，升序
a.sort(reverse=True)        # 原地排序，降序
b = sorted(a)               # 返回新数组，不修改 a

# 自定义排序键
words = ["banana", "fig", "apple"]
words.sort(key=len)         # 按长度排序
words.sort(key=lambda x: x[-1])  # 按最后一个字母排序

# 多级排序：先按第一元素升序，再按第二元素降序
pairs = [(1, 3), (2, 1), (1, 2)]
pairs.sort(key=lambda x: (x[0], -x[1]))
# [(1, 3), (1, 2), (2, 1)]
```

### 遍历

```python
a = ['a', 'b', 'c']

for x in a:
    print(x)

for i, x in enumerate(a):
    print(i, x)             # 0 a / 1 b / 2 c

# 同时遍历两个数组
for x, y in zip([1, 2, 3], ['a', 'b', 'c']):
    print(x, y)
```

### 常用技巧

```python
# 扁平化二维数组
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]  # [1, 2, 3, 4, 5, 6]

# 统计元素个数
a = [1, 2, 2, 3, 3, 3]
from collections import Counter
c = Counter(a)              # Counter({3: 3, 2: 2, 1: 1})
c.most_common(2)            # [(3, 3), (2, 2)]

# 去重（不保序）
unique = list(set(a))

# 去重（保序）
seen = set()
unique = [x for x in a if not (x in seen or seen.add(x))]

# 前缀和
a = [1, 2, 3, 4, 5]
prefix = [0] * (len(a) + 1)
for i in range(len(a)):
    prefix[i+1] = prefix[i] + a[i]
# prefix = [0, 1, 3, 6, 10, 15]
# 子数组 a[l:r+1] 的和 = prefix[r+1] - prefix[l]
```

---

## 哈希（dict）

### 创建

```python
d = {}
d = dict()
d = {'a': 1, 'b': 2}
d = dict(a=1, b=2)

# 从两个列表构建
keys = ['x', 'y', 'z']
vals = [1, 2, 3]
d = dict(zip(keys, vals))   # {'x': 1, 'y': 2, 'z': 3}
```

### 增删改查

| 操作 | 写法 | 时间复杂度 |
|------|------|-----------|
| 写入 / 更新 | `d[k] = v` | O(1) 均摊 |
| 读取 | `d[k]` | O(1)，键不存在抛异常 |
| 安全读取 | `d.get(k, default)` | O(1) |
| 删除 | `del d[k]` | O(1) |
| 弹出 | `d.pop(k, default)` | O(1) |
| 是否存在 | `k in d` | O(1) |
| 键数量 | `len(d)` | O(1) |

```python
d = {'a': 1}

d['b'] = 2          # 新增
d['a'] = 99         # 更新
d.get('c', 0)       # 0，键不存在时返回默认值
del d['b']          # 删除
d.pop('a', None)    # 删除并返回值，不存在也不报错
```

### 遍历

```python
d = {'x': 1, 'y': 2, 'z': 3}

for k in d:                  # 遍历键
    print(k)

for v in d.values():         # 遍历值
    print(v)

for k, v in d.items():       # 遍历键值对
    print(k, v)
```

### defaultdict

不用每次先检查键是否存在：

```python
from collections import defaultdict

# 值是 int（适合计数）
count = defaultdict(int)
for c in "hello":
    count[c] += 1            # 不存在的键自动初始化为 0

# 值是 list（适合分组）
groups = defaultdict(list)
for word in ["cat", "car", "bar", "bat"]:
    groups[word[0]].append(word)
# {'c': ['cat', 'car'], 'b': ['bar', 'bat']}

# 值是 set
graph = defaultdict(set)
graph['a'].add('b')
```

### 哈希表常用模式

```python
# 1. 频率统计
from collections import Counter
s = "abracadabra"
freq = Counter(s)
freq['a']          # 5
freq.most_common(2)  # [('a', 5), ('b', 2)]

# 2. 两数之和（经典）
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i

# 3. 滑动窗口 + 哈希（无重复字符最长子串）
def length_of_longest_substring(s):
    pos = {}
    left = 0
    best = 0
    for right, c in enumerate(s):
        if c in pos and pos[c] >= left:
            left = pos[c] + 1
        pos[c] = right
        best = max(best, right - left + 1)
    return best

# 4. 分组 anagram
from collections import defaultdict
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())
```

---

## 选哪个？

| 场景 | 用 list | 用 dict |
|------|---------|---------|
| 有序数据、按下标访问 | ✓ | |
| 需要快速判断存在性 | | ✓ O(1) vs list O(n) |
| 键值映射关系 | | ✓ |
| 频率/计数统计 | | ✓ Counter |
| 图邻接表 | | ✓ defaultdict(list) |
| 双指针/滑动窗口 | ✓ | 辅助用 dict |

---

## 时间复杂度总结

| 结构 | 查找 | 插入（末尾）| 插入（中间）| 删除 |
|------|------|------------|------------|------|
| list | O(n) | O(1) 均摊 | O(n) | O(n) |
| dict | O(1) 均摊 | O(1) 均摊 | — | O(1) |
| set  | O(1) 均摊 | O(1) 均摊 | — | O(1) |

dict 和 set 在极端情况下（哈希碰撞）会退化到 O(n)，但面试和日常使用基本不用考虑。

---

这张表覆盖了 90% 的刷题场景。两数之和、滑动窗口、分组这三个模板多写几遍，基本上哈希类题目就能应付了。
