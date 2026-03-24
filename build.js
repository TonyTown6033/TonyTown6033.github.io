// ========== 构建脚本 ==========
// 用法：node build.js
// 扫描 data/*.md，生成 posts.json（文章列表）

var fs = require("fs");
var path = require("path");

var DATA_DIR = path.join(__dirname, "data");
var OUTPUT = path.join(__dirname, "posts.json");

// 解析 frontmatter（和 server.js 里一样的逻辑）
function parseFrontmatter(text) {
  if (!text.startsWith("---")) {
    return { title: "", date: "", summary: "" };
  }

  var endIndex = text.indexOf("---", 3);
  if (endIndex === -1) {
    return { title: "", date: "", summary: "" };
  }

  var frontStr = text.substring(3, endIndex).trim();

  var meta = {};
  frontStr.split("\n").forEach(function (line) {
    var colonIndex = line.indexOf(":");
    if (colonIndex !== -1) {
      var key = line.substring(0, colonIndex).trim();
      var value = line.substring(colonIndex + 1).trim();
      meta[key] = value;
    }
  });

  return {
    title: meta.title || "",
    date: meta.date || "",
    summary: meta.summary || ""
  };
}

// 扫描 data/*.md
var files = fs.readdirSync(DATA_DIR).filter(function (f) {
  return f.endsWith(".md");
});

var posts = files.map(function (filename) {
  var text = fs.readFileSync(path.join(DATA_DIR, filename), "utf-8");
  var meta = parseFrontmatter(text);
  return {
    filename: filename,
    title: meta.title,
    date: meta.date,
    summary: meta.summary
  };
});

// 按日期倒序
posts.sort(function (a, b) {
  return b.date.localeCompare(a.date);
});

fs.writeFileSync(OUTPUT, JSON.stringify(posts, null, 2), "utf-8");
console.log("构建完成！生成 posts.json，共 " + posts.length + " 篇文章");
