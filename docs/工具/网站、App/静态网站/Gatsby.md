# Gatsby

Gatsby 是一个基于 React 的静态页面生成器。

## 项目结构

```text
/
|-- /.cache             自动生成
|-- /plugins            本地插件
|-- /public             生成的输出
|-- /src
    |-- /pages          页面
    |-- /templates      模板
    |-- html.js
|-- /static             这里的文件不会被webpack处理，而是直接复制到public中
|-- gatsby-config.js    主配置文件
|-- gatsby-node.js
|-- gatsby-ssr.js
|-- gatsby-browser.js
```

## CLI

`gatsby new`：创建新项目。

`gatsby develop --host 0.0.0.0 --port 8000 --open`：开发服务器，`--open`自动打开浏览器。

`gatsby build`：生成可用于生产环境的文件到 public。

`gatsby repl`：交互式 shell。

## 内置 React 组件

### <Link\>

基于 @reach/router，非常智能，能自动基于用户界面和用户行为预加载。

只要把所有的非外链的`<a>`换成`<Link>`。

```diff
-<a href="/blog">Blog</a>
+<Link to="/blog">Blog</Link>
```

具体见 [Gatsby Link API](https://www.gatsbyjs.com/docs/reference/built-in-components/gatsby-link/)。

## 路由 Routing

这里指的是 URL 路径的创建。三种方式创建：

1. `src/pages`中的 React 组件
1. 用 File System Route API
1. 在`gatsby-node.js`中用`createPages`

