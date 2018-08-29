这篇文章暂用于测试Markdown及$\LaTeX$是否正常运作，也可用于简单学习一些特殊的Markdown命令(请查看Github上的源文件来看代码)

基本的Markdown命令可在网上搜索优秀的学习资源进行学习，本网站还支持了一些特殊的命令，基于Material for MkDocs[^1]。更多的具体情况请查看 [此链接](https://squidfunk.github.io/mkdocs-material/extensions/admonition/)

## 代码测试

``` Python
import numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])
for z in x:
    print(z+y)
```

## 数学公式测试

行间公式：

$$
\frac{n!}{k!(n-k)!} = \binom{n}{k}
$$

行内公式：$p(x|y) = \frac{p(y|x)p(x)}{p(y)}$

## 文字增删及高亮测试

有时为了更准确地将文本的变动记录下来，增删的过程都要体现出来， {--删除的文字--} 会被加上删除线同时配上红色的底色， {++增加的文字++}会被加上下划线同时配上绿色的底色. 就像这样： NKDACS是南开大学{~~统计研究院~>统计与数据科学学院~~}成立的一个科研组织。

此外，还可以对文字进行{==高亮==} 操作。

甚至还可以以作者身份加一条评论对某个部分进行点评{>>我觉得这样挺棒的！<<}.

## Emoji

网站还支持Emoji表情😂，你可以前往[emojicopy.com](https://www.emojicopy.com/)复制一些Emoji表情粘贴在Markdown文件里，网站可以正常地将他们展现出来😎

## Task list

网站支持下面样式的Task list，效果很棒

* [x] 学术分享
* [x] 教程制作
* [x] 讨论班
* [ ] 网站制作
    * [x] 基本设计
    * [x] 样式设计
    * [ ] 服务器维护
    * [ ] 正式发布
* [ ] NKDACS正式展开活动

它的Markdown代码很简单，只用像下面这样写就可以了：

``` markdown
* [x] 学术分享
* [x] 教程制作
* [x] 讨论班
* [ ] 网站制作
    * [x] 基本设计
    * [x] 样式设计
    * [ ] 服务器维护
    * [ ] 正式发布
* [ ] NKDACS正式展开活动
```

## Note

网站支持通过特殊Markdown代码来设计如下的Note样式

!!! note "这是一个小Note"
    可以在这个可爱的小Note中记录一些要点，这样的样式更能吸引读者的眼球，从而将你想要表达的重点凸显出来。
    Note中依然可以正常使用各种形式的Markdown。无论是数学格式还是代码格式，都能正常地包含在Note中。

    设计这种note很简单，它的Markdown代码如下：

    ``` markdown
    !!! note "这是一个小Note"
            可以在这个可爱的小Note中记录一些要点，这样的样式更能吸引读者的眼球，从而将你想要表达的重点凸显出来。
            Note中依然可以正常使用各种形式的Markdown。无论是数学格式还是代码格式，都能正常地包含在Note中。
    ```

### 折叠显示

可以像下面这样对部分文字进行折叠操作，通过鼠标点击可以展开/收回文字块，从而能满足一些特殊场景下的需求

??? note "NKDACS是由学生与老师共同参与的项目组织吗？"

    是的，NKDACS有强大的教授团体对项目组的学生进行学术指导。

默认是收起来的，当然，改为默认展开也是可以的

???+ note "NKDACS是由学生与老师共同参与的项目组织吗？"

    是的，NKDACS有强大的教授团体对项目组的学生进行学术指导。

## 其他测试

### 列表测试

* 数学与应用数学
* 统计学
* 信息与计算

### 表格测试

First Header | Second Header | Third Header
:----------- |:-------------:| -----------:
居左         | 居中        | 居右
居左         | 居中        | 居右
居左         | 居中        | 居右
居左         | 居中        | 居右
居左         | 居中        | 居右
居左         | 居中        | 居右

## 注脚测试

注脚系统可用于参考文献的引用排版。

下面展示注脚效果：

本网站基于MkDocs[^1]系统，采用了Material for MkDocs[^2]主题样式，感谢开源社区的贡献！
[^1]: [https://www.mkdocs.org/](https://www.mkdocs.org/)
[^2]: [https://squidfunk.github.io/mkdocs-material/](https://squidfunk.github.io/mkdocs-material/)