# jsblog

纯 HTML/CSS/JavaScript 个人博客项目，无框架依赖。

## 项目结构

```
jsblog/
├── index.html       # 页面入口
├── style.css        # 样式
├── app.js           # 核心逻辑（渲染、导航）
└── data/            # 文章数据
    ├── post1.js     # 每篇文章一个文件，定义 postN 变量
    ├── post2.js
    └── posts.js     # 汇总：const posts = [post1, post2, ...]
```

## 技术栈

- 原生 JavaScript（无框架、无构建工具）
- Markdown 渲染：marked.js（CDN 引入）
- 直接用浏览器打开 index.html 运行

## 开发约定

- 文章数据放在 `data/` 目录，每篇文章一个独立 `.js` 文件
- 文章文件命名：`postN.js`，变量命名：`const postN = { ... }`
- 新增文章需要同步更新 `index.html`（添加 script 标签）和 `data/posts.js`（添加到数组）
- 文章 content 字段使用 Markdown 格式
- 不使用任何构建工具或包管理器
