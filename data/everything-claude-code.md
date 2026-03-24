---
title: Everything Claude Code：让 AI 编程助手更强大的插件
date: 2026-03-24
summary: 介绍 Everything Claude Code (ECC) 插件，一套让 Claude Code 战斗力翻倍的 skills、agents 和 hooks 集合。
---
如果你在用 Claude Code 写代码，那你一定要了解一下 **Everything Claude Code**（简称 ECC）。这是一个社区驱动的开源插件，给 Claude Code 装上了一整套"技能包"。

## ECC 是什么

简单来说，ECC 是一个 Claude Code 插件，它包含了：

- **Skills** — 预定义的工作流程，比如测试驱动开发、代码审查、安全扫描
- **Agents** — 专门的子代理，可以并行处理任务
- **Hooks** — 自动触发的脚本，在特定事件发生时执行
- **Rules** — 编码规范和最佳实践

装上之后，你就可以用各种斜杠命令来调用这些能力。

## 核心功能一览

### 代码质量

`/simplify` 会审查你改过的代码，检查是否有重复、低效或可以优化的地方。`/code-review` 则做更全面的代码审查。

针对不同语言还有专项审查：
- `/typescript-review` — TypeScript/JavaScript
- `/python-review` — Python
- `/rust-review` — Rust
- `/go-review` — Go

### 测试

`/tdd` 是我最喜欢的功能之一。它会引导你按照"先写测试、再写实现"的流程来开发，确保代码有足够的测试覆盖。

`/e2e` 则帮你生成和运行端到端测试，用的是 Playwright。

### 规划

写代码之前先想清楚怎么做，`/plan` 会帮你分析需求、拆解步骤、识别风险。`/blueprint` 更厉害，一句话描述目标就能生成详细的执行计划。

### 构建修复

代码编译报错了？各语言都有对应的 build-fix：
- TypeScript 构建错误
- Rust 的 borrow checker 问题
- Go 的 vet 警告
- C++ 的链接错误

它们会自动定位问题并用最小改动修复。

### 安全

`/security-review` 扫描你的代码，检查 OWASP Top 10 漏洞，包括注入攻击、XSS、不安全的加密等。`/security-scan` 则检查你的 Claude Code 配置本身是否安全。

### 文档和学习

`/docs` 可以查询库和框架的最新文档。`/codebase-onboarding` 能分析一个陌生的代码库，生成上手指南，帮你快速理解项目。

## 怎么安装

ECC 是 Claude Code 的官方插件，安装很简单：

```bash
claude plugin add everything-claude-code
```

安装完成后，在 `~/.claude/settings.json` 里确认插件已启用：

```json
{
  "enabledPlugins": {
    "everything-claude-code@everything-claude-code": true
  }
}
```

## 实际使用场景

举几个我日常用到的场景：

**写新功能前**：先跑 `/plan`，让它帮我理清思路和步骤，避免写到一半发现方向不对。

**写完代码后**：跑 `/simplify`，看看有没有可以精简的地方。

**接手别人的项目**：用 `/codebase-onboarding` 快速了解项目结构和关键模块。

**多任务并行**：用 `/orchestrate` 或 `/devfleet` 让多个 agent 同时工作，比如一个写代码、一个写测试。

## 小结

ECC 本质上是把社区积累的最佳实践打包成了即插即用的工具。不管你是刚开始用 Claude Code，还是已经用了一段时间，装上 ECC 都能让你的开发体验上一个台阶。

项目地址：[GitHub - anthropics/everything-claude-code](https://github.com/anthropics/everything-claude-code)
