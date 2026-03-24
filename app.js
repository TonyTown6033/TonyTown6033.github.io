// ========== DOM 元素 ==========
var app = document.getElementById("app");
var navLinks = document.querySelectorAll("nav a");

// ========== 解析 frontmatter ==========
// 从 .md 文本中提取正文部分（跳过 frontmatter）
function getContent(text) {
  if (!text.startsWith("---")) {
    return text;
  }
  var endIndex = text.indexOf("---", 3);
  if (endIndex === -1) {
    return text;
  }
  return text.substring(endIndex + 3).trim();
}

// ========== 渲染函数 ==========

// 渲染首页（文章列表）
function renderHome() {
  fetch("posts.json")
    .then(function (res) {
      return res.json();
    })
    .then(function (posts) {
      var html = "";
      for (var i = 0; i < posts.length; i++) {
        var post = posts[i];
        html +=
          '<div class="post-card">' +
          '<h2 onclick="renderPost(\'' + post.filename + '\')">' + post.title + "</h2>" +
          '<span class="date">' + post.date + "</span>" +
          '<p class="summary">' + post.summary + "</p>" +
          "</div>";
      }
      app.innerHTML = html;
    });
}

// 渲染文章详情
function renderPost(filename) {
  // 先从 posts.json 拿元数据，再 fetch .md 文件拿正文
  fetch("posts.json")
    .then(function (res) {
      return res.json();
    })
    .then(function (posts) {
      var meta = posts.find(function (p) {
        return p.filename === filename;
      });

      return fetch("data/" + filename).then(function (res) {
        if (!res.ok) {
          throw new Error("文章加载失败：" + res.status);
        }
        return res.text();
      }).then(function (text) {
        var content = getContent(text);
        app.innerHTML =
          '<div class="post-detail">' +
          '<a class="back" onclick="renderHome()">\u2190 返回首页</a>' +
          "<h2>" + meta.title + "</h2>" +
          '<div class="date">' + meta.date + "</div>" +
          '<div class="content">' + marked.parse(content) + "</div>" +
          '<div id="comments"></div>' +
          "</div>";

        // 动态加载 utterances 评论（innerHTML 里的 script 不会执行，必须用 createElement）
        var script = document.createElement("script");
        script.src = "https://utteranc.es/client.js";
        script.setAttribute("repo", "TonyTown6033/TonyTown6033.github.io");
        script.setAttribute("issue-term", "title");
        script.setAttribute("theme", "github-light");
        script.setAttribute("crossorigin", "anonymous");
        script.async = true;
        document.getElementById("comments").appendChild(script);
      });
    });
}

// 渲染关于页
function renderAbout() {
  app.innerHTML =
    '<div class="about">' +
    "<h2>关于我</h2>" +
    "<p>你好！我是一个正在学习 JavaScript 的开发者。</p>" +
    "<p>这个博客是我的练手项目，用来记录学习过程。</p>" +
    "</div>";
}

// ========== 导航切换 ==========
navLinks.forEach(function (link) {
  link.addEventListener("click", function (e) {
    e.preventDefault();

    navLinks.forEach(function (l) {
      l.classList.remove("active");
    });
    this.classList.add("active");

    var page = this.getAttribute("data-page");
    if (page === "home") {
      renderHome();
    } else if (page === "about") {
      renderAbout();
    }
  });
});

// ========== 初始化 ==========
renderHome();
