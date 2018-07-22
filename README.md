# NKDACS-Website

南开大学统计咨询网站(基于Flask)

# 示例
本网站暂时部署在 [http://115.159.186.240:8080](http://115.159.186.240:8080)

用户名:nkdacs

密码:demo

# 基于以下框架
- [Python](http://python.org/)
- [Flask](http://flask.pocoo.org/)
- [MongoDB](http://www.mongodb.org/)
- [Bootstrap 3](http://getbootstrap.com/)
- [jQuery](http://jquery.com)
- [Lightbox 2](https://github.com/lokesh/lightbox2)
- [Markdown](http://daringfireball.net/projects/markdown/syntax)
- [Polymer](http://www.polymer-project.org)


# 功能
- 创建/预览/更新/删除 文章;
- 创建/更新/删除 用户;
- 搜索;
- RSS.

# 文章编辑器
- WYSIWYG Markdown editor;


# 配置要求
- mongoDB >= 2.2


# 部署方法
`git clone https://github.com/NKDACS/NKDACS-Website.git`

`cd NKDACS-Website`

(可选)`virtualenv --no-site-packages ./env`

(可选)`source ./env/bin/activate`

`pip install -r requirements.txt`


修改 `config.py`

- 将变量`CONNECTION_STRING`替换为你自己的数据库服务器;

- 将变量`DATABASE`替换为你自己想要设置的;

- 正式发布时，将`DEBUG`变量改为`False`.

# 运行
在本地(或远程服务器上)运行好所需的数据库服务，之后在终端运行

`python web.py`

![builtin_run](http://i.imgur.com/dkEL5aS.png?2)

或者

`gunicorn web:app`

![gunicorn_run](http://i.imgur.com/rCp0g25.png?2)


# 关于 WYSIWYG 编辑器:
WYSIWYG 编辑器基于 [Markdown](http://daringfireball.net/projects/markdown/syntax). Only available on the editor panel tags are intepreted.

![wysiwyg_editor_panel](http://i.imgur.com/D6aFuLT.png)

依赖项目为 [MDMagick](https://github.com/fguillen/MDMagick) .

# 之前写的工作流程

之前的工作流程转移到 [WORK-README.md](https://github.com/NKDACS/NKDACS-Website/blob/dev/WORK-README.md)
