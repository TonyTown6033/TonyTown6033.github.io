+++
title = "南京大学ics进度"
date = 2026-02-23T11:31:52+08:00
draft = false 
description = '记录南京大学ics 操作系统前导课的进度'
tags = []
categories = []
series = []
summary = '记录南京大学 ICS 课程推进：完成 pa1、pa2，下一步进行 diff-test 验证。'
showTableOfContents = true
+++

## Background

最近在做南京大学的 ICS。它是操作系统课之前的一段前导训练，用软件把一台计算机一点点搭起来。平时我们习惯直接调用系统，很少去想底层是怎么呼吸的；这门课刚好反过来，逼你从细节开始。

课程地址在这里：[ics-nju](https://nju-projectn.github.io/ics-pa-gitbook/ics2024/)

我自己的代码仓库在这里：[ics2024](https://github.com/TonyTown6033/ics2024)

## Notes

到目前为止，我做完了这些：

- `pa1`
  1. 环境安装完成
  2. `expr.c` 已支持基础计算（`+`、`-`、`*`、`/`、解引用、读取地址）
  3. 随机表达式测试用例完成

- `pa2`
  1. 选择 `riscv32` 架构，并补充了部分 `riscv32` 指令
  2. 完成 `stdio.c`、`string.c`，并通过测试

接下来要做的事很明确：用 `diff-test` 去验证当前系统的正确性。
