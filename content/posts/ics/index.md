+++
title = "南京大学ics进度"
date = 2026-02-23T11:31:52+08:00
draft = false 
description = '记录南京大学ics 操作系统前导课的进度'
tags = []
categories = []
series = []
summary = ''
showTableOfContents = true
+++

## Background

南京大学ics 是操作系统的前导课程，主要是通过软件来模拟计算机运行的过程。
该课程的地址是[ics-nju](https://nju-projectn.github.io/ics-pa-gitbook/ics2024/) 
对应的代码仓库我保存在[这里](https://github.com/TonyTown6033/ics2024)


## Notes
我会将已经完成的内容写在下面：

- `pa1`
  1. 环境安装
  2. `expr.c` 完成了计算的基本功能（`+`、`-`、`*`、`/`、解引用、读取地址）
  3. 随机计算测试用例也完成了

- `pa2`
  1. 使用 `riscv32` 架构，补充了一些 `riscv32` 指令
  2. 补充了 `stdio.c`、`string.c` 并通过了测试

接下来要做的是用 `diff-test` 验证当前系统的正确性
