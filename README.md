# TonyTown Blog

一个基于 **Hugo + Blowfish** 的个人博客项目，主要记录技术实践与生活随笔。

## 项目特点

- 使用 Hugo 静态站点生成，构建速度快。
- 使用 Blowfish 主题（Git Submodule）。
- 内容目录清晰：文章按 `content/posts/<slug>/index.md` 管理。
- 已接入 GitHub Pages CI/CD 自动部署。
- 已预留评论能力（当前配置为 `utterances`）。

## 目录结构

```text
.
├── content/                 # 站点内容
│   └── posts/               # 文章目录（每篇文章一个文件夹）
├── archetypes/              # 新文章模板
├── layouts/                 # 自定义模板覆盖（例如 comments partial）
├── assets/                  # Hugo 管道资源（图片、样式等）
├── scripts/new-post.sh      # 新建文章脚本
├── .github/workflows/       # CI/CD（GitHub Actions）
└── hugo.toml                # 站点配置
```

## 环境要求

- Hugo Extended（建议 `0.155.3`）
- Git（支持 submodule）

## 本地运行

```bash
hugo server -D
```

打开 `http://localhost:1313` 预览，改动会自动热更新。

## 本地构建

```bash
hugo --gc --minify --cleanDestinationDir
```

构建产物在 `public/`。

## 如何新写文章

推荐使用仓库脚本，自动生成标准路径和 front matter。

### 方式一：使用脚本（推荐）

```bash
scripts/new-post.sh "你的文章标题"
```

常用参数：

```bash
# 自定义 slug
scripts/new-post.sh "你的文章标题" --slug your-post-slug

# 指定 section（默认 posts）
scripts/new-post.sh "你的文章标题" --section posts

# 直接发布（draft=false）
scripts/new-post.sh "你的文章标题" --publish
```

脚本会创建文件：

```text
content/posts/<slug>/index.md
```

### 方式二：手动创建

```bash
hugo new content/posts/your-post-slug/index.md
```

然后编辑正文与 front matter。

### 方式三：手机发 Issue 自动发布（最省事）

仓库已提供 Issue 模板：`Mobile Post`。

使用步骤：

1. 在 GitHub App 或网页中创建 Issue，选择 `Mobile Post` 模板。
2. 保持标题前缀为 `[Post]`，填写正文 `Content`。
3. 提交后会自动生成文章文件并推送到仓库：
   - 路径：`content/posts/issue-<issue号>/index.md`
4. 系统会在 Issue 下自动回帖，给出文章文件路径和访问链接。

触发工作流文件：`.github/workflows/issue-post.yml`

## front matter 建议

文章头部常用字段（来自 `archetypes/default.md`）：

- `title`：文章标题
- `date`：发布时间
- `draft`：是否草稿（发布前改为 `false`）
- `description`：简短描述（用于摘要/SEO）
- `summary`：列表页摘要（建议手写）
- `tags` / `categories` / `series`：分类信息（可选）
- `showTableOfContents`：是否显示目录

## 发布流程

1. 本地写完文章并确认 `draft = false`。
2. 本地预览：`hugo server -D`。
3. 提交并推送到 `main`（或提 PR）。
4. GitHub Actions 自动构建并部署到 GitHub Pages。

## CI/CD 说明

工作流文件：`.github/workflows/hugo.yml`

- `push` 到 `main/master`：构建 + 部署
- `pull_request` 到 `main/master`：仅构建校验（不部署）
- 可手动触发：`workflow_dispatch`
