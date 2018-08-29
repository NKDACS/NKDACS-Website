# NKDACS-Website

欢迎来访NKDACS！

NKDACS-Website的全部内容均已开源，欢迎各位向本Repo贡献代码！

## 网站结构

此站点为静态站点，通过MkDocs对Markdown文件进行渲染生成html文件，托管于Github Pages以供访问。

## 基于以下工具

* MkDocs：**快速，简单，美观**的静态站点生成器
* Markdown：**简洁，强大**的轻量级标记语言
* MathJax：一个跨浏览器的JavaScript库，用于支持$\LaTeX$

## 网站特点

* Material Design：一种特殊的现代化设计语言，能够使网站组件更有质感。在此，特别感谢开源项目[MkDocs-Material](https://github.com/squidfunk/mkdocs-material)，本站点采用了这一主题设计，并作了少量修改，使得网站能够显示得更加美观。
* 丰富的Markdown支持：采用了开源项目[pymdown-extensions](https://github.com/facelessuser/pymdown-extensions/)，网站的Markdown支持度得到了非常大的提升。
* 全站HTTPS：网站全站支持HTTPS，用户的访问流量得到了加密保护，可防止他人窥探或篡改网站浏览数据。

## 为什么采用MkDocs？

网站设计初期，我们的考虑是使用传统的Django或者Flask框架来制作这一网站，但经过小组成员的反复探讨，认为NKDACS-Website的实际设计和使用需求并不太适合用前两者来完成，而轻量、易用的MkDocs成为了我们最终的选择，主要的原因有下：

* 作为一个知识共享平台，NKDACS-Website应该是一个有严格逻辑框架的网站，将会有着广而深的框架式学术内容，传统的博客框架更多地基于时间顺序结构，以及简单的分类和标签结构，而MkDocs作为Wiki化的文档管理系统，与本网站的需求一拍而合。
* 上手简单、易维护。NKDACS是一个学生团体，而学生的学籍变动快，一旦负责网站设计、维护的同学毕业离校，将会存在网站交接的难题，MkDocs上手简单、设计规范、无需进行服务器维护，对比传统的Django/Flask框架，更适合学生团队持续运营。

## 如何指出NKDACS-Website上的错误，以及如何在这个平台上分享知识？

我们已将网站的全部文章的Markdown源码开源于此[Repo](https://github.com/NKDACS/NKDACS-Website)的docs文件夹内，而网站的所有页面均直接基于这些Markdown文件进行渲染生成，因此，您只需要修改相应的文件然后提交Pull Request，我们会根据采用情况进行Merge，或者您也可以针对具体的情况在[Repo](https://github.com/NKDACS/NKDACS-Website)内提出Issues，我们会做出相应的回应。

**具体的操作指导将会补充在此处。**