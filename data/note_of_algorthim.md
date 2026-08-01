---
title: cpp 使用到的一些技巧 
date: 2026-08-01
summary: note some trick when i do algorthm
---

## priority_queue 
```cpp
using Entry = std::pair<int,int>;
std::priority_queue<Entry, std::vector<Entry>, std::greater<Entry>>heap;
```
priority_queue是一个小根堆, 就是说push_back元素后，会自动排序的数据结构
however priority_queue dont have the emplace_back instead of emplace

std::greater<Entry> meas to sort by big to end, heap.top() is the bigest element of the heap;


## iterator
```cpp
using EntryIterator = std::list<Entry>::iterator;

std::list<Entry> entries_; // front: LRU, back: MRU
std::unordered_map<int, EntryIterator> positions_;
```
iterator for me is kind of pointer to the data , its behavior same
std container support this kind of operator , like 
- container.earse(iterator)
- container.splice(target_iterator, target_container, src_iterator)

waring:
- container.end() does not means the end of the container , you could see code like this to prove
```cpp
auto it = list.find(key);
if (it != list.end()) {
    // if exist code 
    ...
}

// if not exist code
```
if you need to use the last iterator of the container you can write like this
```cpp
auto it = std::prev(container.end());
```






