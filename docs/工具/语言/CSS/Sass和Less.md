# Sass 和 Less

这两个都是 CSS 的衍生，在 CSS 的基础上加入了变量、嵌套等高级特性，并最终编译回正常 CSS 使用。

## Sass

[Sass](https://sass-lang.com/) 有两套语法，最开始是缩进语法，文件拓展名是`.sass`，后来发现大家喜欢 CSS 本身的`{}`加`;`语法，又搞了个 SCSS，文件扩展名是`.scss`。两个风格不同而已，都可以使用。以下以 SCSS 为例。

特性：

1. 变量：`$primary-color: red;`
1. 嵌套：用`{}`嵌套，相当于`ul li`
1. 部分、模块：带`_`开头的文件名，不会被编译至 CSS 文件，可以在其它 Sass 文件中用 `@use` 引用为模块
1. Mixin：
1. TODO

## Less

另一个。
