---
title: cpp 使用到的一些技巧 
date: 2026-08-01
summary: note some trick when i do algorthm
---

## priority_queue 
```cpp
using Entry = std::pair<int,int>;
std::priority_queue<Entry, std::vector<Entry>, std::greater<Entry>> heap;
```

这里的 `std::greater<Entry>` 会让 `priority_queue` 成为小根堆，
因此 `heap.top()` 是堆中最小的元素。对于 `std::pair<int, int>`，
默认先比较 `first`，`first` 相同时再比较 `second`。

`priority_queue` 只保证堆顶元素符合优先级，不会把所有元素完整排序。
插入元素使用 `push()` 或 `emplace()`，没有 `push_back()` 或 `emplace_back()`。


## iterator
```cpp
using EntryIterator = std::list<Entry>::iterator;

std::list<Entry> entries_; // front: LRU, back: MRU
std::unordered_map<int, EntryIterator> positions_;
```

迭代器可以理解为一种用于访问容器元素的“指针”，但它并不等同于普通指针。
例如，`std::list` 支持通过迭代器删除或移动元素：

- `entries_.erase(iterator)`
- `entries_.splice(target_iterator, entries_, source_iterator)`

`end()` 返回尾后迭代器，它位于最后一个元素之后，不能被解引用。
`find()` 没有找到目标时通常会返回这个迭代器：

```cpp
auto position = positions_.find(key);
if (position != positions_.end()) {
    EntryIterator entry = position->second;
    // 找到了 key
}
```

只有当容器非空且支持双向迭代时，才能使用 `std::prev()` 取得最后一个元素：

```cpp
if (!entries_.empty()) {
    auto last = std::prev(entries_.end());
}
```
