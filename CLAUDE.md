# jsblog

纯 HTML/CSS/JavaScript 个人博客项目，无框架依赖。

## 项目结构

```
jsblog/
├── index.html       # 单页入口
├── app.js           # 前端核心逻辑（SPA 渲染、导航）
├── style.css        # 全站样式
├── build.js         # 构建脚本（Node.js）
├── posts.json       # 构建产物：文章元数据列表
└── data/            # 文章 Markdown 文件（带 YAML frontmatter）
```

## 技术栈

- 原生 JavaScript（ES5 风格：var、function，无箭头函数）
- Markdown 渲染：marked.js（CDN 引入）
- 评论系统：utterances（GitHub Issues 驱动）
- 构建：`node build.js` 生成 posts.json
- 无包管理器，无框架

## 开发约定

- 文章放在 `data/` 目录，每篇一个 `.md` 文件，kebab-case 命名
- 文章 frontmatter 格式：
  ```yaml
  ---
  title: 标题
  date: YYYY-MM-DD
  summary: 摘要
  ---
  ```
- 新增文章后运行 `node build.js` 重新生成 posts.json
- 本地预览需要 HTTP 服务器（`npx serve .` 或 `python3 -m http.server`），fetch 不支持 file://
- 不使用任何构建工具或包管理器（build.js 除外）

## 构建与运行

- 构建文章索引：`node build.js`
- 本地预览：`npx serve .` 然后打开 http://localhost:3000
